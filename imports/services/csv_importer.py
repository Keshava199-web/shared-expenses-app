import pandas as pd

from imports.models import ImportJob, ImportAnomaly

from datetime import datetime

from decimal import Decimal
from django.contrib.auth.models import User
from expenses.models import Expense

from expenses.models import ExpenseParticipant

class CSVImporter:

    def __init__(self):
        self.import_job = None
        self.seen_expenses = set()
    
        self.meera_leave_date = datetime.strptime(
            "31-03-2026",
            "%d-%m-%Y"
        ).date()

        self.sam_join_date = datetime.strptime(
            "15-04-2026",
            "%d-%m-%Y"
        ).date()

    def import_file(self, file_path):
        self.import_job = ImportJob.objects.create(
            file_name=file_path.name,
            status="pending"
        )

        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            self.process_row(index + 1, row)

        self.import_job.status = "completed"
        self.import_job.save()

        return self.import_job
    
    def detect_duplicate_expense(self, row_number, row):
        description = str(
            row.get("description", "")
        ).strip().lower()

        amount = str(
            row.get("amount", "")
        ).strip()

        key = (description, amount)

        if key in self.seen_expenses:
            self.create_anomaly(
                row_number=row_number,
                issue="Possible duplicate expense",
                action="Marked for manual review"
            )
        else:
            self.seen_expenses.add(key)

    def process_row(self, row_number, row):
        self.detect_missing_payer(row_number, row)
        self.detect_missing_currency(row_number, row)
        self.detect_negative_amount(row_number, row)
        self.detect_duplicate_expense(row_number, row)
        self.detect_settlement(row_number, row)
        self.detect_membership_violation(row_number, row)

        expense = self.create_expense(row)

        if expense:
            self.create_participants(
                expense,
                row
            )

    def detect_missing_payer(self, row_number, row):
        if pd.isna(row.get("paid_by")):
            self.create_anomaly(
                row_number=row_number,
                issue="Missing payer",
                action="Manual review required"
            )

    def detect_missing_currency(self, row_number, row):
        if pd.isna(row.get("currency")):
            self.create_anomaly(
                row_number=row_number,
                issue="Missing currency",
                action="Defaulted to INR"
            )
        
        def detect_settlement(self, row_number, row):
            description = str(
                row.get("description", "")
            ).lower()

            notes = str(
                row.get("notes", "")
            ).lower()

            keywords = [
                "paid back",
                "settlement",
                "deposit",
                "reimbursement"
            ]

            for keyword in keywords:
                if keyword in description or keyword in notes:
                    self.create_anomaly(
                        row_number=row_number,
                        issue="Settlement detected",
                        action="Should be imported as Settlement"
                    )
                    break

    def create_anomaly(self, row_number, issue, action):
        ImportAnomaly.objects.create(
            import_job=self.import_job,
            row_number=row_number,
            issue_type=issue,
            action_taken=action
        )

    def detect_membership_violation(self, row_number, row):
        try:
            expense_date = datetime.strptime(
                str(row.get("date")),
                "%d-%m-%Y"
            ).date()

            participants = str(
                row.get("split_with", "")
            ).lower()

            if (
                "meera" in participants and
                expense_date > self.meera_leave_date
            ):
                self.create_anomaly(
                    row_number=row_number,
                    issue="Meera included after leaving",
                    action="Manual review required"
                )

            if (
                "sam" in participants and
                expense_date < self.sam_join_date
            ):
                self.create_anomaly(
                    row_number=row_number,
                    issue="Sam included before joining",
                    action="Manual review required"
                )

        except Exception:
            pass

    def create_expense(self, row):
        payer_name = str(
            row.get("paid_by", "")
        ).strip()

        try:
            payer = User.objects.get(
                username__iexact=payer_name
            )
        except User.DoesNotExist:
            return None

        try:
            expense_date = datetime.strptime(
                str(row.get("date")),
                "%d-%m-%Y"
            ).date()
        except Exception:
            return None

        expense = Expense.objects.create(
            group_id=1,
            title=str(
                row.get("description", "")
            ),
            amount=Decimal(
                str(row.get("amount", 0))
            ),
            currency=str(
                row.get("currency", "INR")
            ),
            expense_date=expense_date,
            paid_by=payer,
            split_type=str(
                row.get("split_type", "equal")
            ).lower()
        )

        return expense
    
    def create_participants(self, expense, row):

        split_type = str(
            row.get("split_type", "")
        ).lower()

        participants = [
            p.strip()
            for p in str(
                row.get("split_with", "")
            ).split(";")
            if p.strip()
        ]

        if not participants:
            return

        if split_type == "equal":
            self.create_equal_split(
                expense,
                participants
            )
        
        elif split_type == "unequal":
            self.create_unequal_split(
                expense,
                row
            )

    def create_equal_split(
        self,
        expense,
        participants
    ):
        share = (
            expense.amount /
            len(participants)
        )

        for username in participants:

            try:
                user = User.objects.get(
                    username__iexact=username
                )

                ExpenseParticipant.objects.create(
                    expense=expense,
                    user=user,
                    share_amount=share
                )

            except User.DoesNotExist:
                pass

    def create_unequal_split(
        self,
        expense,
        row
    ):
        details = str(
            row.get("split_details", "")
        )

        entries = details.split(";")

        for entry in entries:

            entry = entry.strip()

            if not entry:
                continue

            try:
                parts = entry.rsplit(" ", 1)

                username = parts[0].strip()

                amount = Decimal(
                    parts[1].strip()
                )

                user = User.objects.get(
                    username__iexact=username
                )

                ExpenseParticipant.objects.create(
                    expense=expense,
                    user=user,
                    share_amount=amount
                )

            except Exception:
                self.create_anomaly(
                    row_number=0,
                    issue="Invalid unequal split",
                    action="Manual review required"
                )
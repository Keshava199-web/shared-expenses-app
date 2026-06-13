from rest_framework.views import APIView
from rest_framework.response import Response

from imports.services.csv_importer import CSVImporter


class ImportCSVView(APIView):

    def post(self, request):
        file = request.FILES.get("file")

        if not file:
            return Response(
                {"error": "CSV file required"},
                status=400
            )

        importer = CSVImporter()

        job = importer.import_file(file)

        return Response({
            "import_job_id": job.id,
            "status": job.status
        })
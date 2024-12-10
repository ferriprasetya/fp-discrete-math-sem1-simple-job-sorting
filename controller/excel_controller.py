from services import upload_excel_job


def upload_list_pekerjaan():
    try:
        return upload_excel_job.upload_list_pekerjaan_excel()
    except Exception as e:
        print(e)
        exit(1)

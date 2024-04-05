import gspread
from oauth2client.service_account import ServiceAccountCredentials
import config.Config as config

json_file_name = config.GOOGLE_AUTH_FILE_NAME
spreadsheet_url = config.GOOGLE_SPREADSHEET_URL

def google_upload(confidence,distance,liveness,result,time):
    scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
    gc = gspread.authorize(credentials)

    # 스프레스시트 문서 가져오기
    doc = gc.open_by_url(spreadsheet_url)

    # 시트 선택하기
    worksheet = doc.worksheet(config.GOOGLE_WORKSHEET)

    #행으로 데이터 추가하기
    worksheet.append_row([confidence, distance, liveness,result,time])

def test_upload():
    google_upload("99.9", "0.3057", "1.00000", "Pass", "" )

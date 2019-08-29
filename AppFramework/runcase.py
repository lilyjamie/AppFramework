from test.util.CeaterRunner import RunCaseAndCreateReport
from test.util.CreateTestSuite import CreateTestSuite
from utils.Log import Log
from utils.Filepath import LOG_PATH
from utils.SendMail import SendMail

log = Log(LOG_PATH)
suite = CreateTestSuite()
suites = suite.choose_all_cases("test*.py")

run = RunCaseAndCreateReport(suites)
run.run()

mail = SendMail()
new_report = mail.new_report()
mail.send_email(new_report)

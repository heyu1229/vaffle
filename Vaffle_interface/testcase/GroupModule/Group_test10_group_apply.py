import unittest,time,json
from Vaffle_interface.public_1.func_requests import FuncRequests


class Group(unittest.TestCase):

    def setUp(self):
        self.r=FuncRequests()

    # -----------------消息中心-请求---------------------------
    def testcase_001(self):
        sheet_index = 14
        row = 11
        member_id = 'e51ae55c-6131-4d20-a31e-6595a932c84b'
        payload = {"page":"1"}
        result = self.r.interface_requests_payload(member_id,sheet_index,row,payload)

        print(result)
        self.assertEqual(10000, result['code'])
        print("code返回值：10000")

if __name__ == "__main__":
    unittest.main()
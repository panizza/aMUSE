from django.test import TestCase, Client
from basetyzer.models import Exhibit
from django.core.urlresolvers import reverse
import json as j

class ItemTest(TestCase):
    fixtures = ['all_data.json']

    def setUp(self):
        self.client = Client()

    def test_get_item_info(self):
        response = self.client.get(reverse('get_item_info', kwargs={'hash_item': '356a452b7913b04c54574d18c28d46e6395428ab'}))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse('get_item_info', kwargs={'hash_item': '356a192b7913b04c54574d18c28d46e6395428ab'}))
        self.assertEqual(response.status_code, 200)


class ExperienceTest(TestCase):
    fixtures = ['percussion_new_db.json']

    def setUp(self):
        self.client = Client()

    def test_save_experience(self):
        """
        TODO[lotto]: moar failing test cases and image
        """

        #working case with no image
        exp_dict = {"exp": [{"id": "2",
                             "date": "2013-05-06 17:42:52",
                             "photo": "",
                             "text": "ne voglio una",
                             "type": "scan"},
                            {"id": "1",
                             "date": "2013-05-06 17:43:30",
                             "photo": "",
                             "text": "master master",
                             "type": "scan"},
                            {"date": "2013-05-06 17:43:56",
                             "photo": "",
                             "text": "questi bonghi mi fanno venire voglia di africa",
                             "type": "personal"}],
                    "confirm": "24e3261d7bbe24664c1babc75189cfebec04498b",
                    "email": "gpinelli@brixen.de"}

        exp_json = j.dumps(exp_dict)

        response = self.client.post('/api/exp/s/', exp_json, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        #working case with image
        exp_dict = {"exp": [{"id": "2",
                             "date": "2013-05-06 17:42:52",
                             "photo": "",
                             "text": "ne voglio una",
                             "type": "scan"},
                            {"id": "1",
                             "date": "2013-05-06 17:43:30",
                             "photo": ( "/9j/4AAQSkZJRgABAQEAeAB4AAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcU",
                                        "FhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgo",
                                        "KCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAA2ADIDASIA",
                                        "AhEBAxEB/8QAGwAAAgIDAQAAAAAAAAAAAAAAAAUCBAEGBwP/xAAyEAABAwMBBQUGBwAAAAAAAAAB",
                                        "AAIDBAURIQYSMUGBEyJRYaEUFVJxkcEHQ3KCseHx/8QAGwEBAAMBAAMAAAAAAAAAAAAABgACBQcB",
                                        "AwT/xAAtEQABAwIEAwcFAQAAAAAAAAABAAIEAxEFITFBBhJRE3GBkbHB0RQiMmHw8f/aAAwDAQAC",
                                        "EQMRAD8AYBSCiOSu0NA6pgkqJQ72dmd1jTh0rhyzyGdPHPhzcTZtKFS7Wr/pRCBBqzqvZUtd+gHU",
                                        "rRNmbnfKra68tusfs9siJipo3ADJDtHN5uyMknhqE1oLtcpdr6y3TULPdjYmyQVTDzwMh2vHOfp5",
                                        "rrG02z1Ts7sLVXG20MtzvFM1kgo6ZxjaRvt32sa0d4hu8RkHJHDkuZWytuV9qo6W4WmsppzR+1tn",
                                        "lJ3YZe6OxII7rtTzzjqjNHGqxe1vLle+ufdoktTBYxY54fmAB+OXfrf+0TkKYVWimM9LFI4Yc5oJ",
                                        "HgeYVkFLA4OAcNCiLmlji06hTQo5QpZRUQtkspbV2PsGuLHMBicRxBHA/PBB6rWhxTGx1Yo64tkO",
                                        "IZ8NJ+F3I9c4+ixOI4jpEXnZqw38N0g4YmtjTOR+jxbx2+F2nZ26C526N7y0VcYDZ2Dk/mR5HiP9",
                                        "XM9q5IaH8QK0g7sdSGNdroJC1uD6Y/cmEb5IZRLTyvhlA0ew4P8AY8jotb2jhjrO3e581XVudmaU",
                                        "uAA+ZGACBjAGvBCaMwAgnUJucLu5zb/a4EfCSWs5pcDk938k/dXmpdbMtnmj3QxoDTug6cxkdAEz",
                                        "aF0XD63bRWP/AF6ZLnGLR/pptSmTv65+6MIU8IX13Wel4CC0OBBGQdCFEPD5TE18LXgZJlkDGj5k",
                                        "/YFMKeKyxAOr7vSzP+Fk4jaOgOT1PRZ07GI8Q8jrud0GfnstTD8FkzbPbZrepy8tyrNur3VUfu2a",
                                        "bcmONx+93nsHEfqxp6+KftpoW04gETBCBjcxokbqrZ+amdTQVdJA0kEGJzWYI4EHxTGC50LIWNku",
                                        "NLI5owX9q0Z8+K51LLatUvpMLQdl0+E19Ci2nWqBzhvotUuUDqCtcT+Wc58WHj6eoV9uo0XttHV2",
                                        "6aFj46ymdM04AbI0kg9UmttfF2TICJy5riwFsL3NxnA7wGOGNcpVw5Kdyuov7x7opxfFY/klU9dD",
                                        "7FNULKEqQdLcDOcarKEL3WVFIKYQhVIUU2lerUIVCopZQhCqvK//2Q=="),
                             "text": "master master",
                             "type": "scan"},
                            {"date": "2013-05-06 17:43:56",
                             "photo": "",
                             "text": "questi bonghi mi fanno venire voglia di africa",
                             "type": "personal"}],
                    "confirm": "24e3261d7bbe24664c1babc75189cfebec04498b",
                    "email": "gpinelli@brixen.de"}

        exp_json = j.dumps(exp_dict)

        response = self.client.post('/api/exp/s/', exp_json, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        def test_wrong_save_experience(self):            
            #bad confirmation code
            exp_dict = {"exp": [{"id": "2",
                                 "date": "2013-05-06 17:42:52",
                                 "photo": "",
                                 "text": "ne voglio una",
                                 "type": "scan"},
                                {"id": "1",
                                 "date": "2013-05-06 17:43:30",
                                 "photo": "",
                                 "text": "master master",
                                 "type": "scan"},
                                {"date": "2013-05-06 17:43:56",
                                 "photo": "",
                                 "text": "questi bonghi mi fanno venire voglia di africa",
                                 "type": "personal"}],
                        "confirm": "347523459836932475294529",
                        "email": "gpinelli@brixen.de"}

            exp_json = j.dumps(exp_dict)

            response = self.client.post(reverse('save_experience'),data=exp_json, content_type='application/json')

            self.assertEqual(response.status_code, 400)

            #nonexisting item id
            exp_dict = {"exp": [{"id": "-44",
                                 "date": "2013-05-06 17:42:52",
                                 "photo": "",
                                 "text": "ne voglio una",
                                 "type": "scan"},
                                {"id": "1",
                                 "date": "2013-05-06 17:43:30",
                                 "photo": "",
                                 "text": "master master",
                                 "type": "scan"},
                                {"date": "2013-05-06 17:43:56",
                                 "photo": "",
                                 "text": "questi bonghi mi fanno venire voglia di africa",
                                 "type": "personal"}],
                        "confirm": "347523459836932475294529",
                        "email": "gpinelli@brixen.de"}

            exp_json = j.dumps(exp_dict)

            response = self.client.post(reverse('save_experience'),data=exp_json, content_type='application/json')

            self.assertEqual(response.status_code, 400)

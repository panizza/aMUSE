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
        
        working_b64 = "/9j/4AAQSkZJRgABAQEASABIAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcg\nSlBFRyB2NjIpLCBxdWFsaXR5ID0gOTAK/9sAQwADAgIDAgIDAwMDBAMDBAUIBQUEBAUKBwcGCAwK\nDAwLCgsLDQ4SEA0OEQ4LCxAWEBETFBUVFQwPFxgWFBgSFBUU/9sAQwEDBAQFBAUJBQUJFA0LDRQU\nFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU/8AAEQgAgACA\nAwEiAAIRAQMRAf/EAB0AAAICAwEBAQAAAAAAAAAAAAYHBQgDBAkCAAH/xAA+EAABAwIEAwUGAwYF\nBQAAAAABAgMEBREABhIhBzFBEyJRYYEIFDJxkaEVI0IJUoKx4fAWJHLB0RclM2Lx/8QAGgEAAwEB\nAQEAAAAAAAAAAAAAAgMEBQEABv/EACIRAAICAgICAgMAAAAAAAAAAAABAhEDIRIxBEEiURNCYf/a\nAAwDAQACEQMRAD8AvPwc9mzJXBKGXqZGMurqTZ2pSTqc8wjokHywfKryXXloSq+nawx+Zhn9jBkO\nW7wFrDC8YqqotNckuK0JVsFHmpRPL7fS+E6gqQa32Ha6shL/ALulz8y3aPKHh0H1/ljQm5gjRklc\n59Ib2KWioJvvtfy8uuASjVdySspau5KkDWpSuiOhPz/3xmg5Mdn1JuoupcnOIUVGQoFTaVH91I52\n5X8MKcm+gkkhowaqqZES+bssnkVDvK8LD/bG4w4spLjx7JN+62o7/M+flgfpQ9xUDJkLfc6XSEAD\nwAxM/izfJLBJ6W3P3wxO+waJNErVuAT5q2x694AuSStfRI2wK1rNkOht9pMeSwf0tuK7yvIJG5ws\npPFauZlqDkamrapFOSbGUUhTit97ef1ttjksiiHHG5DuW86UEqJJJ/RskeV+vzxjjOaTqUtN/I4W\nNPablxrSJ8mU4fjdkOHV8gB/e+Jaj1VilTUNi+gmwJVfC1l3sZ+J0MV4B1pxBx827+U2TzsL4wMS\nA7pVyUdiMekdzSk7i5T/AMYoJ6Pp8VubGdYcGpt1JBHzxzK4yZCmcP8AiHmOnyGldk9KVIjPaSA4\n2sXBB5Hnvjp1upPmMIv2peFbOdMoO1BlZjzoaSvtkcy3+oH03HUYRnhyhYUdOik2TswMRmfc5UZB\njx7kk8lnoMQ+fnae0piFUYaNK0F6MkLPcvvuPDGSS7/h2YWKZIStgAF9MhOpS/MYga9CVnB67j6i\n+0dWnl3PDGOkk7OnTjM9TDi0sJUTrBBCfPAHmAR5tQiwnHnGafGSFOJZAKnFKNg2CeRO/TkCcS+b\nGlQcwJQh7QgoBsT/AHviv3Far12sVFmLleVHaZiuF6dOlPhpnbbSDuTZOrcC1zfGxkdIKKse8LMe\nUmp0mDIktx3vhcZjajYeCl35/LC/4wcbZXB+K7UqRW1KpqUflRXRdLdhyA5kfPFKG86ZlzRnOc8m\notU+EZCkoDThVqsfiKgR3fAAXPPlgtqkmm1KCC647WGEqKZEl03B7hUQnw2BBte1wMTOTehsYosR\nwr9sKs8QIMYZjiR6Y9IRraUpBTqQb2UCk9QOWGBJztTltKLU5+U6B2pbZfWhpI/eWb8vLCUyjk+k\nZ2q2Wm32Qn37tCkAadOhsixt4bADEjnjLbmWcqsQoy+zXPnGO9ffuoTsk+CTz+gxznKrYaim6RNK\nzAjNFQVKVJc/Dmz39AN3ze1hfp4D1OCqkV6mw3WnJj7NPYHdDCEKWlA87D7nGLhvkpqTS20dsFOl\nI1KI6/2cLH2gzn/hq2f8OUZ+THWCo1Bl5CUt/wCoKIvhNyeytRS0O7/qRlGVJLLeY47chJ+BxWgH\n1O2Np2stB9sx5SXgdwUqCvuMcqeKNc4lVLPH4LmFxqqaUB9D8RAKxqSCAlaLX52PmDh7cG6vmfh5\nGyplaCw7Vs4ZvlXplMlv6NLSNluKUr4UgXufI+GOzUk0vZ6MlTfo6uw2FJaQVcylJ+2NooC0qtz5\nj54xw0uCMyHSkuhtIWUX06rC9r9L3xspTZXzxrJGO2eErJTfEbXqYcw5cnwxbU8ytsah4pIGN9Ys\nCMeXp7NOiuPOqDbTaStajyAHPHatUzhyvzlSHqlmQOsIMd1l8wnUEd1vSdKifPbAHmaox8pT5Ko5\nDs8KVHsTfV/TB9xIq0incXc9xyox9VSccQykbBCzqSr1BBwvMyU+DU6eJgdtLbWpJUdySB/PGI1T\noM6J5lqzU2qPFUgMspTqcWeQSPP74q/xdpmUqUqp0Wm5icqlcqilyHH+0/LiIUrmGwd12NgVbDbY\nnlYCl0KZWIc1xyV7p2jSiXyAS0m25AOEHEyfRuGCq5mKVEVWMx1NztYzEgAtpWAQkhPUk97e9tvA\nY0cgyIoZuRopESl0mCptQKEOSStSlhB3NxsBcg+ZFiTyGHTljhfHVS6dS1BLrarNuFQtqAUQeX+s\neh8sB3BJmtzc/wBSpuZStyfKaE1ZUlILalBfdNgBulJIHTQBh4VzL02lO0+pRVEI96CHADsEkW38\nNxz88Ir2NN/M+Vxw9zdRJMW7MdmpKU2kbApU2kKHrcn0wQcWcrOVfKEmZEGp5qWmoJT1KdAS4kel\nz6Yjs8TXuIHDBUnQWqpT3mn16eYLah3h802wzKJLZlxEx3wFNPAOIBO1invJ9Qb/APzHqUrXphRk\n41IR+R8/OUVSEOuHuj9WG+nMtH4gUJ6BLaQ+l1JQUk8xbFauLVGkZYqciJHQo6FHQoHZSen2xg4a\nZhmtSkalqQsH4b7YgWSUHxZsOEci5IdHDn2dKFlWpzJ61LW2s6W2Xne1CE3va5+ww0KTwiyu5xJo\nechT0Jq1KprtNivDbQ2tYWbDlfnc87euFfnSpZtgZXYreWoEeuz4Kw6KRJkdiJIsbkK5XGxAPPfr\ngd4B+0ZxT4rVx9upcOYlAocOYuJMqSJoU2y43YrSm9itXeAsBbfc4txSSdUQZoXHbLmsuA2IO2Ns\nAHcYFqPVkTD3HAsHqDe2Cdo6mxjSTsyGqMEoqBTpwn/aVz03kThdXJqpXuq3WDGaXfcLc7ot57k+\nmHM6nUgnHO79onn5UioUjLbTpUhtKpa2grbXcpST6BWByPjFs6isVOdTOr02pSZkiWQoBx191Tjj\nlhYXJ3xu1GQ3Mp7nYNFuOo3UsDZKyOWIXKE5hymrQQlLzh1E8ziOar7SpUhpxa0IU7ZtrVZCj42x\njy22EdRMwVmFlWE9EejqeGhLj1r79Ug+XlhDS+LwdzpHi1DL0CBOlJLrCpLqSWGgO6paRdSSraw2\nNueGHxRzpCgVgVF17vPqDLLYspKEpG6gnqroL4pDx84mRqOurzKaoSq1VHy02lCisMFVgNSuq9IG\nw874ulJuVIfFUrHV7NMmp504wZ/zNPU2HFKRALbfwoU0VlOnyUg3HzOLMUeI1XVz6W7YBxPvDO5v\ndO/8zbFM/ZF4hO01HuikKFOqEptyNLWg2JUg2GrruFpIO4VbxxbnKlSk0159byD79BUpsgj42z8K\nvkdsdddHAqhZXZYpykBtNpLYbfR0JKbG/wBcQNQqrlMy5BeRqC47aFFSeYKNv5X++CfKFebrCXUp\nNlJYQpV+eoEj+VvpiHrMZFSpU9lJHaRlErQOZB3/AJK+2Af8CT+xf58qcOtQ/flgLUlJVqHLb4k/\ncG3hhVTc1RafZunxEPSyfy9awlJPiT4Ynq9CrVHzUqliMqTTnSyk6UlQUFJUFG3PbUPv4YTOXazT\nhXJlMrD4jyYjxYUXPiFiQDfzGIMqd2amKfx4ktWuJfHLJsiU7Sqjk6cp0/klbq3FNJts3ZY0JPTU\nRa/UYtj7K1FztUOFqapnr8ORWao+ZzcaEhJCG1JG7ikWSpajubXtYC53xV/L/s80bipxQpryK5Jd\npMNPvM+Gw6UdskGyU6km4ClEAnwvi/GRW24ERiEy0GWWkBpKECyEJSLADw2AxZ46vZH5M/1PkFVF\nlIWEgIKrXPT0GGPSZiZMZKgeeBitU0SoTwsCR3hfyx6ynLIbLalEgbXAsL4vWmZ72GDhG4HM446+\n1PmpzOPHXNbvKHDeVT2Ara4buCfUgn1GOwhQXCNyLkY4f8QJJqGes0uTFOLcaqcoDSOoeUN8Jzv4\ngog8saos9pIUWkqBStR72kHrgir2VqdS6UibqXoekAJWtYKlr/8AUDlgSfblNU17sUEXsSoHp0GN\nqsZldrTFMivIDDcZHZpSgbE+PzxBVsIvNxF4NzqhRn3a3UQwWCqQ8pKu9HaSP/EDyClqKQT0Gw3J\nxz1zJl9WcuMMSn0h1c6ElxSmvdySEWSEDlyIJJ8r88OTPPtEZx4vkUGL2yYz8hfaojklcjQL6B5a\n1JTfqST4Ysf7M/snwuHVFZnVFKJGZJSEKlvg3S2blXZNjwBJueZt4ADFDlwVrssjDlp9Epwh4KLy\nXkZtpthuQ72aRJQ4kkKI3B0m/Lodz54e0KCmoxYNTaQDJS12UlCd0uJ5b/3zGJ6l0hyAWzH090ab\nL5KHgcYBSk0WrKlMtusxJG7zSBqLC7/GE/qbP6rbjna3IYNrTDyRT2iEp1GVQMxKlMajClMdmUk/\nA4CbA+ijbEQ1NXAzHV+21BCkp7vXSUWv98N12kJnwnQ2lBcUjax2KhyI9cLzMNF97Lc9KdIeQWHe\nikFJ6/K5H0wyUa6EJ32DGZwJbslbCtL4CXQkCxISlN7fLngXzfwQylxEnIn1ijNvoqCUvJlR1ll5\nCyPzE602PPob4O4NNVIXKamNqbU2saFD9SFJ2I+49Bjcy4DQy9R6gjVHCu0jOcwBYcj4f1wtq3sN\nNpaBfgvkHLPCtM6FQoHYKecAdeedU666Ae6FLUb2G9gLAXw4KLODststJ/LUSTY2B88AH4SunOuP\noPaoJU7cczbkPrbBVlx1NIhIQ+4FjYkn9KjzHphmK1oXk3sa0dtLzek2NxiOp0T3OouNWCUndNsf\nlGqzcptopN7beWNuY2pMtt1PXFggn0WCQRt1xxV9oij/AIBx34iRIqjGLVZlq57WUsr5fxY7TtXW\nyAeeORHtyUhuie1Bn0vNfkS0x5KLfqUthF/W4OE51cTkeyvy3VsU91wuKWru7JP1wRMpdqtHZLYj\nKjMKK3VJA7ZN/LnbGn+FCFRZiiPzFlsII3ATbGtTWnC+hzvgrJbK0p5gjyxBf0H7LF8N+F6MhZ2Y\ngx2kyXYaEjt1i6lOKJJNugGq/mSPAYuflOYIkVpDqu0WLXJ6nFacoZgbqOYajV3ykOvunSByAwzl\nZtU20CyN/HCXkuTZsRx/FIsRCJlISQbX3wQQoLZYs4Aon97fCOyxxDW52SFOAlPj1wzqRnBElpNy\nATz8sUwnGQmcJIJnErZC+xSO2G7Y6LIHw/M4xLhxapHdUlsJdWApSFJ332uR48wcacuvxgz3lgX5\nEHHzFTVLnQZLfeafb0laeRWBc3+Y39DimMk9EUotbBGu01zsiwm7T6dTaVAdOh9DY/XGrBjqzHl9\n9vsgmcwQpIsLk8yn7X88HGaaUanGS9GIKkalG3OxwO0unrY96fFyFg9oOSkqG99vE7+WONUzyeiP\nyy+ylCY00BCgojvdArcffGrUQ2uW8hThU6zsW08r+PrzxvVeCagh+QgBMhKT3gPiNtr+Bv1woMxZ\n6bpucExW9SZ7No76QCCQEggqBFuuxHQ47B06Bkr2PDJstxDYCr6krsbnlgwqFY93Ui24PM9BhdcP\nKumoC5GjVYkX5YP6hTVvRlNlQ1J3SpI+2HroWFFOl9swLbm2Oa/7SyCzC4uwJCIri3JtKadWtI7o\n0OKRv6bY6IZYlkxg04bqRtcbY5+/tRFORc+ZWlNLKdVGcQ4kH4h7wbXH1wOTcDi7KXSMwuzo81tx\nAa0WSgW3sOWNylVCVTolOLii2lIEhJvsrflgZbkqeeDxN9auad7HBvKZD0KEmoSYzsdcclsxebQ8\nCPHGe1QTGvkavudslGrdZuMNn8SdVIYbCyU2urffFfeGL/4nIfmJXdtt3sm7HbYbnDzh2cSwsG6z\na4tjNnqVH0WN2rGLk10uSgTuPnywx26wYI1FelIHLCky9PTCWCogqJttsLYIKhWwttWlXw8wepwy\nD4o9JWwjzBnRYZIQ4U7dTyw0OGtYdRktmVIUNK3ghF9rWR/Q4qvmHMzcRh19TiR2YKrc+nhhqnNM\n1PCzJz0RaLqpQqTyj+88QE7f6CvFWCVybIvIiqSG5SM+NqnzYhcJdiK0utjfnsD8t8TlPdbmf5li\n/e7q03vfCs4aMIl5uqRcdS4ZzAkMpJsSUgBSSOfMD64a1HpiYb0ptpdihwhST1uLpV9DY+YxbFtm\nc6R+fhDi3n0oACjZSAeSxY4V/GHha7KlxqvHDjiDpPZhelKFpGwNvW1/LDiU44ltZZKe1ACtKjb5\ng/8AOPbktmvUWQyW7KKChxlfMHww1JA2xF5QqTK32m4xkx3EAFxx5kpCrbdxQJ1c+tsWLo6FvQ2Q\n+Va9IKSsb2thLZNyr2VYbS+rteycsu5KU89tuuxv88PdKUR2gE2ASLDyw1C2aiWUQpSiAnST42xT\n79pJw/j1bh7RM2pbbL1PecgPLVe4bcGtNjb95BH8WLXzqulS1anErSFabBQuFeHjhfcd8gPcaOC+\nbMpRnEIqEmJ20EqVYCQ2QtsHbYEp0/xY49qjpxVpbiYsZald5SXiCk9RgtpNHj15lsCaqICnUpC+\nYA8PHA1PgSINRdhyGDHlsuKS8yoboWm4UD5gi2JiDV9NIW2UpL2gIQTzaT1N8Z80/R19BtwurDUP\nLUX3dZUl1a3AVJsd1dR0w68v1ovRkk8+m+KzcNpK5dCZUF6ihxSFb8iD/XD2yaSpjcm4HLEmaKUm\nzawSuKQex67Z0NqNhfcnniYk1zUhSgoFXLSDzwvaoXWlarDa3eHPGFmoq7YLuQSmxxOVGfPNW/7Z\nKBV+hW17c9sPrhPmOl5o4UZUaW8Ap6lroytW4bdZJ0g/wnn5YrXmxldUpy4zNjLlENt36qJ2xL5G\nfnZdqFJytCf1uMvJkOJB2TpSQVbdVXP++KcDoi8jZbTJNSVlCrxDJT/mk62SCN0JIFyPmUj0xtcJ\n+MMmtcRc2UiqlsAuF6GRyW0eh8Nzb53wteKlefy9SoeYy8jRDfRHk2uopbUU6Vm29k3P1xFzZ7Rm\nRa6zEejvJQp33qPfSop7xbWkbbgEpJtexHPFSk4uiFq0WWzzUFiM3PiSuyeYIQtxKyO6tPcUfGyt\nj9cRPD7iE9XabHclo92qqBpeSkEpKkmy09L7g2wp6JnoZwotVgrf7smCl9lw3BSSbg+VtSeW9x5Y\nlOHGYPfMzP0hxpxEso7TtVXBW4ltKlqA6ggn5KFuuGcrdgca7GDxC4s0HhRQ3MxVgrfZCtSWGR3l\nAW+p32+eAXgp7dVK47ViVDoWWa1GjMqKfe5LIDR62uCbG29jgC9u+nSYnD+WkpTNpSW2nXmlKALK\nQ5ZageaTpJIO4uncYUPsN8WaZQF5vyYZbAnJfMiCpZSn3iyLbE9SLbeOH8nQCSujoDIzDHbdedbL\nYk6R2izpCRfcBV7X9CMQnE3OFboPC3MGYaC5HZq1Pird1PAqSlIIupIuSbC5APlijWfPbFqUepVW\nOmmByMw4W/z2kuA6VaCd9rknTiXz77V0incEJVFiFh+tVkdm0ho2EWOTqWVc+XwjxwKyWw5QpFQs\n5ZhM3PE6pOOtzPfnlyNbdwlWsk3++/njxS1pkzZTyYw7oBJJ2SAOVsRWYEIm+7S2glCuzupKeigd\n8SGUGX349VlJ3bCFJUBzNxYAYU1asR6P/9k=\n"
        
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
                             "photo": working_b64,
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

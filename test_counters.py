from playwright.sync_api import Page, Route
import pytest

@pytest.mark.parametrize("co2, energy, water, num", [(-138,0,10,1), (1000,93731,12000,2), (100.1737333,2.7575757571,10.77444,3), (1006354353453543534537434329,7224735435643,109344444,4),
(0.0000000001, -0.0000000001, 0, 5), (0.49999999999999999, 0.50000000000000001, 0.5, 6), ("ABC", True, "@", 7),
(1.49999999999999999, 1.50000000000000001, 1.5, 8)])
def test_mock_eco_impact_api(page: Page, co2, energy, water, num):
    def handle(route: Route):
        json = {
            "result": {
                "blocks": {
                    "personalImpact": {
                        "avatarUrl": "https://static.avito.ru/stub_avatars/%D0%9E/7_256x256.png",
                        "data": {
                            "co2": co2,
                            "energy": energy,
                            "materials": 0,
                            "pineYears": 0,
                            "water": water
                        }
                    }
                },
                "isAuthorized": True
            },
            "status": "ok"
        }
        route.fulfill(json=json)
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle)
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-wrapper-OutiE").screenshot(path="output/screenshot" + str(num) + ".png")

def test_mock_different_browsers(page: Page):
    page.set_viewport_size({"width": 500, "height": 1200})
    def handle(route: Route):
        json = {
            "result": {
                "blocks": {
                    "personalImpact": {
                        "avatarUrl": "https://static.avito.ru/stub_avatars/%D0%9E/7_256x256.png",
                        "data": {
                            "co2": 50,
                            "energy": 4321,
                            "materials": 0,
                            "pineYears": 0,
                            "water": 21
                        }
                    }
                },
                "isAuthorized": True
            },
            "status": "ok"
        }
        route.fulfill(json=json)
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle)
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-wrapper-OutiE").screenshot(path="output/screenshot9.png")
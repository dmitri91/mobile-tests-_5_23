import json
from datetime import datetime

import allure
import requests
from allure_commons.types import AttachmentType

import config


def add_video(session_id):
    # video_url = ("https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4")

    response = requests.get(f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
                            auth=(config.settings.userName, config.settings.accessKey))

    video_url = response.json()["automation_session"]["video_url"]

    html = (
        "<html><body><video width='100%' height='100%' controls autoplay><source src='"
        + video_url
        + "' type='video/mp4'></video></body></html>"
    )

    allure.attach(
        body=html,
        name='video_' + session_id,
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )


def add_screenshot(browser, name):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png,
        name=name,
        attachment_type=AttachmentType.PNG,
        extension='.png',
    )


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(
        body=html,
        name='page_source',
        attachment_type=AttachmentType.HTML,
        extension='.html',
    )
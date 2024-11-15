"""
File: account.py
Author: Dmitry Ryumin
Description: Event handler for Gradio app to account.
License: MIT License
"""

import gradio as gr

# Importing necessary components for the Gradio app
from app.config import config_data


def event_handler_account(account: str, surname: str, username: str) -> tuple[
    gr.Button,
    gr.Textbox,
    gr.Textbox,
    gr.Dropdown,
    gr.HTML,
]:
    is_account_hidden = account != config_data.OtherMessages_HIDE_ACCOUNT

    return (
        gr.Button(
            value=(
                config_data.OtherMessages_HIDE_ACCOUNT
                if is_account_hidden
                else (
                    f"{surname} {username}"
                    if not config_data.AppSettings_QUALITY
                    else surname
                )
            )
        ),
        gr.Textbox(visible=is_account_hidden),
        gr.Textbox(visible=is_account_hidden),
        gr.Dropdown(visible=is_account_hidden),
        gr.HTML(elem_classes=None if is_account_hidden else "step-2"),
    )

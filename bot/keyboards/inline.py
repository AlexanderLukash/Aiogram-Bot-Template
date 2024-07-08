# Function to create the main menu inline keyboard
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def test_keyboard():
    buttons = [
        [
            InlineKeyboardButton(
                text="🧪 Test",
            ),
        ],
    ]

    # Creating an InlineKeyboardMarkup object with the defined buttons
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons,  # List of button rows
    )
    return keyboard  # Returning the created inline keyboard

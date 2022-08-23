## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABjQtEXjJdgVlImuWhsLkUOZmAY6s4SUI9JE06zGGdASGdD6LuZrsJ8fxP9WlSUjWXydVeksc7rbfzpXDe6A_RFarYj05Oun-YdQcFreQl-HA7yeeDvAeBzvWcqxFUpf8zwllYRpa3bZZaShqM_qAvgvzaf6uFcIC4nUhJhXhrrAUoR6TY_rvppcTFE1Q3lr-GYenyEz3SiRFFgGjFZIElm1S5Fi_D4qDqlMGryKqu2vd40tHRdTnXK_q6HRmXMR6eQGiQSeXTiwUT_4ni1x4YSg_uEG1RVYbnDHDX0V2oxqIFBuVqwJFdPNWSgD4B7ndmmh_Cg3kQjDGxprrxVkAD7AAAAAUvBdQYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5351917074:AAFwS64L_Lc4C0M9a00Cwhsfearc6Iqm6hU")
BOT_NAME = getenv("BOT_NAME", "⋆𝘽𝙊𝙏₊· ͟͟͞͞➳❥❬ 𝕂𝕀𝕃𝕎𝔸 ❭✦❄")
API_ID = int(getenv("API_ID", "11265059"))
API_HASH = getenv("API_HASH", "3d566d6fe2e6b6a522f13e875bd2eb61")
OWNER_NAME = getenv("OWNER_NAME", "✧ꔷˡᵉᵃᵈᵉʳ♪𝙈𝘼𝙉𝙎 🧸💕 ˝❄›.")
OWNER_USERNAME = getenv("OWNER_USERNAME", "M_A_N_S_21")
ALIVE_NAME = getenv("ALIVE_NAME", "✧ꔷˡᵉᵃᵈᵉʳ♪𝙈𝘼𝙉𝙎 🧸💕 ˝❄›.")
BOT_USERNAME = getenv("BOT_USERNAME", "M_A_N_S578BOT")
OWNER_ID = getenv("OWNER_ID", "5545885396")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "D_A_R_K_21")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BAR_M_E_S_E_L_H_Y")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "M_8_S_H")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")

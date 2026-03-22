# “””
🌙 DreamBook Telegram Bot (Gemini хувилбар)

Хэрэглэгч зүүдээ бичихэд Gemini AI гурван өнцгөөс тайлбарладаг.

ТОХИРУУЛАХ ЗААВАР:

1. Доорх TELEGRAM_TOKEN болон GEMINI_API_KEY-г өөрийнхөөрөө солино
1. pip install python-telegram-bot google-generativeai
1. python dreambook_bot.py
   “””

import logging
import google.generativeai as genai
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
Application, CommandHandler, MessageHandler,
CallbackQueryHandler, filters, ContextTypes
)

# ============================

# ⚙️ ЭНИЙГ ӨӨРЧИЛ

TELEGRAM_TOKEN = “8727200546:AAGtGwPcfVDyDByKsmTJIQCaMH8j0SDnFoU”
GEMINI_API_KEY = “ЭНЭД_GEMINI_API_KEY_ОО_ТАВ”  # AIzaSyDL7N1Q… гэж эхэлдэг
DREAMBOOK_PDF_LINK = “https://gumroad.com/l/dreambook-mn”

# ============================

logging.basicConfig(
format=”%(asctime)s - %(name)s - %(levelname)s - %(message)s”,
level=logging.INFO
)
logger = logging.getLogger(**name**)

# Gemini тохируулах

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(“gemini-1.5-flash”)

# Хэрэглэгч тайлбар хүссэн эсэхийг хадгалах

user_state = {}

SYSTEM_PROMPT = “”“Чи DreamBook — Монгол хэл дээрх зүүдний тайлбарын AI туслагч.

Хэрэглэгч зүүдээ тайлбарлуулахад ЗААВАЛ дараах гурван өнцгөөс тайлбарла:

🏹 МОНГОЛ УЛАМЖЛАЛТ ТАЙЛБАР:
Монгол шаманизм, ардын итгэл үнэмшил, өвөг дээдсийн заншлын үүднээс тайлбарла.

🔬 ЮНГИЙН СЭТГЭЛ СУДЛАЛЫН ТАЙЛБАР:
Карл Юнгийн архетип, нийтийн ухамсар, анима/анимус, сүүдэр зэрэг ойлголтоор тайлбарла.

🧠 ФРЕЙДИЙН ТАЙЛБАР:
Зигмунд Фрейдийн ухамсрын доорх хүсэл, репресс, либидо, superego зэрэг ойлголтоор тайлбарла.

Эцэст нь 💡 ЕРӨНХИЙ ДҮГНЭЛТ хий — энэ зүүд юуг хэлж байгааг товч тайлбарла.

Хариу нь дулаахан, ойлгомжтой, Монгол хэлээр байх ёстой. Хэт урт биш, тус бүр 2-3 өгүүлбэр.”””

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
“”“Bot эхлэх команд”””
keyboard = [
[InlineKeyboardButton(“🌙 Зүүдээ тайлбарлуулах”, callback_data=“interpret”)],
[InlineKeyboardButton(“📖 DreamBook PDF авах”, url=DREAMBOOK_PDF_LINK)],
[InlineKeyboardButton(“ℹ️ Тусламж”, callback_data=“help”)],
]
reply_markup = InlineKeyboardMarkup(keyboard)

```
await update.message.reply_text(
    "🌙 *DreamBook Bot-д тавтай морил!*\n\n"
    "Зүүдэндээ ямар нэгэн зүйл харав уу? "
    "Би гурван өнцгөөс тайлбарлаж өгнө:\n\n"
    "🏹 Монгол уламжлалт тайлбар\n"
    "🔬 Юнгийн сэтгэл судлал\n"
    "🧠 Фрейдийн тайлбар\n\n"
    "Доорх товчийг дарж эхэлцгээе! 👇",
    parse_mode="Markdown",
    reply_markup=reply_markup
)
```

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
“”“Тусламжийн команд”””
await update.message.reply_text(
“🌙 *DreamBook Bot ашиглах заавар:*\n\n”
“1️⃣ /start — Эхлэх\n”
“2️⃣ /dream — Зүүдээ тайлбарлуулах\n”
“3️⃣ Зүүдний талаар аливаа зүйл бичихэд хариу өгнө\n\n”
“💡 *Зөвлөгөө:* Зүүдийнхээ тухай дэлгэрэнгүй бичих тусам тайлбар нь нарийн болно!\n\n”
“📖 Дэлгэрэнгүй тайлбарыг DreamBook PDF-ээс уншаарай.”,
parse_mode=“Markdown”
)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
“”“Товч дарсан үед”””
query = update.callback_query
await query.answer()

```
if query.data == "interpret":
    user_state[query.from_user.id] = "waiting_dream"
    await query.message.reply_text(
        "✍️ *Зүүдээ бичээрэй!*\n\n"
        "Зүүдэндээ юу харсанаа дэлгэрэнгүй тайлбарлаарай. "
        "Жишээ нь:\n\n"
        "_\"Би далайд сэлж байсан, гэнэт аварга том загас намайг дагаж эхэллээ...\"_\n\n"
        "Бичиж эхэлнэ үү 👇",
        parse_mode="Markdown"
    )
elif query.data == "help":
    await query.message.reply_text(
        "🌙 *DreamBook Bot ашиглах заавар:*\n\n"
        "Зүүдийнхээ тухай текст бичихэд AI тайлбарлаж өгнө.\n"
        "Илүү дэлгэрэнгүй бичих тусам тайлбар нарийн болно!\n\n"
        "📖 Бүрэн гарын авлагыг DreamBook PDF-ээс уншаарай.",
        parse_mode="Markdown"
    )
elif query.data == "buy_pdf":
    await query.message.reply_text(
        f"📖 *DreamBook PDF авах:*\n\n"
        f"500+ зүүдний дэлгэрэнгүй тайлбар бүхий гарын авлага!\n\n"
        f"👉 {DREAMBOOK_PDF_LINK}",
        parse_mode="Markdown"
    )
```

async def interpret_dream(update: Update, context: ContextTypes.DEFAULT_TYPE):
“”“Зүүдийг Claude-аар тайлбарлах”””
user_id = update.effective_user.id
dream_text = update.message.text

```
# /dream командыг арилгах
if dream_text.startswith("/dream"):
    dream_text = dream_text.replace("/dream", "").strip()
    if not dream_text:
        user_state[user_id] = "waiting_dream"
        await update.message.reply_text(
            "✍️ Зүүдээ бичээрэй:"
        )
        return

# Хэт богино текст
if len(dream_text) < 5:
    await update.message.reply_text(
        "🌙 Зүүдийнхээ тухай арай дэлгэрэнгүй бичнэ үү?"
    )
    return

# Тайлбарлаж байна гэдгийг мэдэгдэх
thinking_msg = await update.message.reply_text(
    "🌙 Зүүдийг тайлбарлаж байна...\n"
    "⏳ Хэдэн секунд хүлээнэ үү."
)

try:
    # Gemini API дуудах
    prompt = f"{SYSTEM_PROMPT}\n\nХэрэглэгчийн зүүд: {dream_text}"
    response = model.generate_content(prompt)
    interpretation = response.text

    # Тайлбар илгээх
    await thinking_msg.delete()

    # PDF худалдах товч нэмэх
    keyboard = [
        [InlineKeyboardButton("📖 DreamBook PDF авах", url=DREAMBOOK_PDF_LINK)],
        [InlineKeyboardButton("🌙 Дахин тайлбарлуулах", callback_data="interpret")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🌙 *Таны зүүдний тайлбар:*\n\n{interpretation}\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📖 500+ зүүдний дэлгэрэнгүй тайлбарыг DreamBook PDF-ээс уншаарай!",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

    # State цэвэрлэх
    user_state.pop(user_id, None)

except Exception as e:
    await thinking_msg.edit_text(
        "⚠️ Алдаа гарлаа. Дахин оролдоно уу."
    )
    logger.error(f"Error: {e}")
```

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
“”“Бүх мессеж боловсруулах”””
user_id = update.effective_user.id
text = update.message.text

```
# Зүүд хүлээж байгаа эсвэл зүүдний тухай бичсэн
await interpret_dream(update, context)
```

def main():
“”“Bot ажиллуулах”””
print(“🌙 DreamBook Bot эхэлж байна…”)

```
app = Application.builder().token(TELEGRAM_TOKEN).build()

# Командууд
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("dream", interpret_dream))

# Товч дарах
app.add_handler(CallbackQueryHandler(button_callback))

# Текст мессеж
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("✅ Bot ажиллаж эхэллээ! Telegram-аас шалгаарай.")
app.run_polling(allowed_updates=Update.ALL_TYPES)
```

if **name** == “**main**”:
main()

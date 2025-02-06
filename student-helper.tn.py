from flask import Flask, request, render_template_string

app = Flask(__name__)

# قاعدة بيانات بسيطة لنصائح المراجعة
def get_study_tips(subject):
    tips = {
        "رياضيات": "قم بحل العديد من التمارين وتأكد من فهمك جيدا للقواعد و أيضًا عليك بكتابة قواعد الجبر أو الهندسة في ورقة بخط واضح وضعها على مكتبك أو علقها و احرص على قراءتها يوميًا و هكذا ستخدع عقلك الباطن و تحفظ القواعد بسهولة.",
        "فيزياء": "ركز على الفهم العملي وحل المسائل المتعلقة بالقوانين الفيزيائية و ركز مع أستاذك في الحصة و راجع التعاريف جيدًا لأن التعاريف يمكنها أن تساعدك في حل المسائل الفيزيائية.",
        "انقليزية": "ركز مع الأستاذ في الفصل و احفظ بعض العبارات كي تستخدمها في الفرض التأليفي و قم بإنجاز بعض التمارين، هذا سيساعدك كثيرًا.",
        "علوم الحياة و الأرض": "احفظ الرسومات التوضيحية وافهم العمليات الحيوية جيدًا.",
        "عربية": "ركز على القواعد و قم ببعض التمارين لحفظها و بالنسبة للإنشاء أنصحك بأخذ بعض العبارات الموجودة في الكتاب التي تناسب المحور الذي تدرس.",
        "فرنسية": "راجع القواعد جيدًا و أما في الإنتاج فعليك بالبحث عن عبارات تناسب المحور الذي تدرسه و احفظها.",
        "تاريخ": "أنصحك بأن تلخص الدروس و تعيد كتابة أهم الأحداث و التواريخ في ورقة أخرى و كذلك في الجغرافيا نفس الشيء، لخص الدروس و اكتب أهم النسب في ورقة أخرى و أنصحك أيضًا في الفصل أن تكتب التواريخ و النسب بلون مغاير كي تخدع عقلك و تحفظ بسهولة.",
        "التربية المدنية": "احفظ أهم التعاريف و افهم الدرس.",
        "أدعية": "هذه أدعية ستساعدك على الحفظ: بعد المراجعة قل 'اللهم إني استودعتك ما حفظت فاللهم رده لي وقت الحاجة'، وقبل الامتحان قل 'اللهم اشرح لي صدري و يسر لي أمري و أحلل العقدة من لساني يفقه قولي اللهم لا سهل إلا ما جعلته سهلا و إنك إن شئت تجعل الحزن سهلا'، و لا تنس الصلاة على الحبيب المصطفى صلى الله عليه وسلم."
    }
    return tips.get(subject, "عذرًا، لا توجد نصائح متوفرة لهذه المادة. عليك الاختيار بين: 'رياضيات-فيزياء-علوم الحياة و الأرض-تاريخ-تربية مدنية-فرنسية-انقليزية-عربية-أدعية'.")

# HTML templates
home_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>تطبيق نصائح المراجعة</title>
</head>
<body>
    <h1>مرحبًا بك في Student-Helper!</h1>
    <form action="/subject" method="post">
        <label for="name">أدخل اسمك:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">التالي</button>
    </form>
</body>
</html>
"""

subject_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>اختيار المادة</title>
</head>
<body>
    <h1>مرحبًا {{ name }}</h1>
    <form action="/tips" method="post">
        <label for="subject">أدخل اسم المادة:</label>
        <input type="text" id="subject" name="subject" required>
        <button type="submit">احصل على النصائح</button>
    </form>
</body>
</html>
"""

tips_page = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نصائح المراجعة</title>
</head>
<body>
    <h1>نصائح المراجعة</h1>
    <p>{{ tips }}</p>
    <a href="/">العودة إلى الصفحة الرئيسية</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_page)

@app.route('/subject', methods=['POST'])
def subject():
    name = request.form['name']
    return render_template_string(subject_page, name=name)

@app.route('/tips', methods=['POST'])
def tips():
    subject = request.form['subject']
    tips = get_study_tips(subject)
    return render_template_string(tips_page, tips=tips)

if __name__ == '__main__':
    app.run(debug=True)
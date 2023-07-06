from django.db import models
from django.core import validators

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    SECTION_CHOICES = (
        ('管理本部', '管理本部'),
        ('財務部', '財務部'),
        ('法務部', '法務部'),
        ('人事部', '人事部'),
        ('営業一部', '営業一部'),
        ('営業二部', '営業二部'),
        ('IT一部', 'IT一部'),
        ('IT二部', 'IT二部'),
        ('広報部', '広報部')
    )

    RANK_CHOICES = (
        ('代表取締役社長', '代表取締役社長'),
        ('常務取締役', '常務取締役'),
        ('専務取締役', '専務取締役'),
        ('本部長', '本部長'),
        ('部長', '部長'),
        ('次長', '次長'),
        ('課長', '課長'),
        ('課長代理', '課長代理'),
        ('係長', '係長'),
        ('社員', '社員')
    )


    LANGUAGE_CHOICES = (
        ('', 'なし'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('JavaScript/jQuery', 'JavaScript/jQuery'),
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('SQL(MySQL)', 'SQL(MySQL)'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('C++', 'C++'),
        ('Ruby', 'Ruby'),
        ('VBA', 'VBA'),
        ('GAS', 'GAS'),
    )

    FRAMEWORK_CHOICES = (
        ('', 'なし'),
        ('Laravel', 'Laravel'),
        ('Ruby on rails', 'Ruby on rails'),
        ('Django', 'Django'),
        ('React', 'React'),
        ('Next.js', 'Next.js'),
        ('Vue.js', 'Vue.js'),
        ('Angular', 'Angular'),
    )

    APPLICATION_CHOICES = (
        ('', 'なし'),
        ('Excel', 'Excel'),
        ('Word', 'Word'),
        ('PowerPoint', 'PowerPoint'),
        ('Access', 'Access'),
        ('Google SpreadSheet', 'Google SpreadSheet'),
        ('GoogleDocs', 'GoogleDocs'),
    )

    Lessoning = models.CharField(
        verbose_name='勉強中プログラミング言語',
        choices=LANGUAGE_CHOICES,
        max_length=200,
        default=None,
        blank=True,
        null=True,
    )
    Lessoning_F = models.CharField(
        verbose_name='勉強中Webフレームワーク', choices=FRAMEWORK_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    Tecnic = models.CharField(
        verbose_name='使用可能プログラミング言語', choices=LANGUAGE_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    Tecnic_F = models.CharField(
        verbose_name='使用可能Webフレームワーク', choices=FRAMEWORK_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    Experience = models.CharField(
        verbose_name='業務経験プログラミング言語', choices=LANGUAGE_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    Experience_F = models.CharField(
        verbose_name='業務経験Webフレームワーク', choices=FRAMEWORK_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    officePC_L = models.CharField(
        verbose_name='勉強中アプリケーション', choices=APPLICATION_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    officePC_T = models.CharField(
        verbose_name='使用可能アプリケーション', choices=APPLICATION_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )
    officePC_E = models.CharField(
        verbose_name='業務経験アプリケーション', choices=APPLICATION_CHOICES, max_length=200,default=None,
        blank=True,
        null=True,
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='年齢',
        validators=[validators.MinValueValidator(18)],
        blank=True,
        null=True,
    )

    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=6000,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True,
    )

    section = models.CharField(
        verbose_name='部署',
        choices=SECTION_CHOICES,
        max_length=200,
    )

    rank = models.CharField(
        verbose_name='役職',
        choices=RANK_CHOICES,
        max_length=200,
    )
    phone = models.CharField(
        verbose_name='電話番号',
        max_length=20,
        blank=True,
        null=True,
    )

    email_add = models.CharField(
        verbose_name='メールアドレス',
        max_length=100,
    )

    postcode = models.CharField(
        verbose_name='郵便番号',
        max_length=10,
        blank=True,
        null=True,
    )

    address = models.CharField(
        verbose_name='住所',
        max_length=50,
    )

    station1 = models.CharField(
        verbose_name='最寄駅１',
        max_length=20,
    )

    employee_number = models.IntegerField(
        verbose_name='社員番号',
    )




    # 管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'


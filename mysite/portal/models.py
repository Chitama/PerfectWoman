from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)





''' 製品テーブル '''
class Product(models.Model):
    # 製品Id
    id = models.AutoField(primary_key=True)
    # 製品名
    product = models.CharField(verbose_name='製品名', blank=True, null=True, max_length=256)
    # ブランド名
    brand = models.CharField(verbose_name='ブランド名', blank=True, null=True, max_length=256)
    # 製品画像
    product_img = models.CharField(verbose_name='製品画像', blank=True, null=True, max_length=256)
    # 成分
    Component_001 = models.CharField(verbose_name='成分001', blank=True, null=True, max_length=128)
    Component_002 = models.CharField(verbose_name='成分002', blank=True, null=True, max_length=128)
    Component_003 = models.CharField(verbose_name='成分003', blank=True, null=True, max_length=128)
    Component_004 = models.CharField(verbose_name='成分004', blank=True, null=True, max_length=128)
    Component_005 = models.CharField(verbose_name='成分005', blank=True, null=True, max_length=128)
    Component_006 = models.CharField(verbose_name='成分006', blank=True, null=True, max_length=128)
    Component_007 = models.CharField(verbose_name='成分007', blank=True, null=True, max_length=128)
    Component_008 = models.CharField(verbose_name='成分008', blank=True, null=True, max_length=128)
    Component_009 = models.CharField(verbose_name='成分009', blank=True, null=True, max_length=128)
    Component_010 = models.CharField(verbose_name='成分010', blank=True, null=True, max_length=128)
    Component_011 = models.CharField(verbose_name='成分011', blank=True, null=True, max_length=128)
    Component_012 = models.CharField(verbose_name='成分012', blank=True, null=True, max_length=128)
    Component_013 = models.CharField(verbose_name='成分013', blank=True, null=True, max_length=128)
    Component_014 = models.CharField(verbose_name='成分014', blank=True, null=True, max_length=128)
    Component_015 = models.CharField(verbose_name='成分015', blank=True, null=True, max_length=128)
    Component_016 = models.CharField(verbose_name='成分016', blank=True, null=True, max_length=128)
    Component_017 = models.CharField(verbose_name='成分017', blank=True, null=True, max_length=128)
    Component_018 = models.CharField(verbose_name='成分018', blank=True, null=True, max_length=128)
    Component_019 = models.CharField(verbose_name='成分019', blank=True, null=True, max_length=128)
    Component_020 = models.CharField(verbose_name='成分020', blank=True, null=True, max_length=128)
    Component_021 = models.CharField(verbose_name='成分021', blank=True, null=True, max_length=128)
    Component_022 = models.CharField(verbose_name='成分022', blank=True, null=True, max_length=128)
    Component_023 = models.CharField(verbose_name='成分023', blank=True, null=True, max_length=128)
    Component_024 = models.CharField(verbose_name='成分024', blank=True, null=True, max_length=128)
    Component_025 = models.CharField(verbose_name='成分025', blank=True, null=True, max_length=128)
    Component_026 = models.CharField(verbose_name='成分026', blank=True, null=True, max_length=128)
    Component_027 = models.CharField(verbose_name='成分027', blank=True, null=True, max_length=128)
    Component_028 = models.CharField(verbose_name='成分028', blank=True, null=True, max_length=128)
    Component_029 = models.CharField(verbose_name='成分029', blank=True, null=True, max_length=128)
    Component_030 = models.CharField(verbose_name='成分030', blank=True, null=True, max_length=128)
    Component_031 = models.CharField(verbose_name='成分031', blank=True, null=True, max_length=128)
    Component_032 = models.CharField(verbose_name='成分032', blank=True, null=True, max_length=128)
    Component_033 = models.CharField(verbose_name='成分033', blank=True, null=True, max_length=128)
    Component_034 = models.CharField(verbose_name='成分034', blank=True, null=True, max_length=128)
    Component_035 = models.CharField(verbose_name='成分035', blank=True, null=True, max_length=128)
    Component_036 = models.CharField(verbose_name='成分036', blank=True, null=True, max_length=128)
    Component_037 = models.CharField(verbose_name='成分037', blank=True, null=True, max_length=128)
    Component_038 = models.CharField(verbose_name='成分038', blank=True, null=True, max_length=128)
    Component_039 = models.CharField(verbose_name='成分039', blank=True, null=True, max_length=128)
    Component_040 = models.CharField(verbose_name='成分040', blank=True, null=True, max_length=128)
    Component_041 = models.CharField(verbose_name='成分041', blank=True, null=True, max_length=128)
    Component_042 = models.CharField(verbose_name='成分042', blank=True, null=True, max_length=128)
    Component_043 = models.CharField(verbose_name='成分043', blank=True, null=True, max_length=128)
    Component_044 = models.CharField(verbose_name='成分044', blank=True, null=True, max_length=128)
    Component_045 = models.CharField(verbose_name='成分045', blank=True, null=True, max_length=128)
    Component_046 = models.CharField(verbose_name='成分046', blank=True, null=True, max_length=128)
    Component_047 = models.CharField(verbose_name='成分047', blank=True, null=True, max_length=128)
    Component_048 = models.CharField(verbose_name='成分048', blank=True, null=True, max_length=128)
    Component_049 = models.CharField(verbose_name='成分049', blank=True, null=True, max_length=128)
    Component_050 = models.CharField(verbose_name='成分050', blank=True, null=True, max_length=128)
    Component_051 = models.CharField(verbose_name='成分051', blank=True, null=True, max_length=128)
    Component_052 = models.CharField(verbose_name='成分052', blank=True, null=True, max_length=128)
    Component_053 = models.CharField(verbose_name='成分053', blank=True, null=True, max_length=128)
    Component_054 = models.CharField(verbose_name='成分054', blank=True, null=True, max_length=128)
    Component_055 = models.CharField(verbose_name='成分055', blank=True, null=True, max_length=128)
    Component_056 = models.CharField(verbose_name='成分056', blank=True, null=True, max_length=128)
    Component_057 = models.CharField(verbose_name='成分057', blank=True, null=True, max_length=128)
    Component_058 = models.CharField(verbose_name='成分058', blank=True, null=True, max_length=128)
    Component_059 = models.CharField(verbose_name='成分059', blank=True, null=True, max_length=128)
    Component_060 = models.CharField(verbose_name='成分060', blank=True, null=True, max_length=128)
    Component_061 = models.CharField(verbose_name='成分061', blank=True, null=True, max_length=128)
    Component_062 = models.CharField(verbose_name='成分062', blank=True, null=True, max_length=128)
    Component_063 = models.CharField(verbose_name='成分063', blank=True, null=True, max_length=128)
    Component_064 = models.CharField(verbose_name='成分064', blank=True, null=True, max_length=128)
    Component_065 = models.CharField(verbose_name='成分065', blank=True, null=True, max_length=128)
    Component_066 = models.CharField(verbose_name='成分066', blank=True, null=True, max_length=128)
    Component_067 = models.CharField(verbose_name='成分067', blank=True, null=True, max_length=128)
    Component_068 = models.CharField(verbose_name='成分068', blank=True, null=True, max_length=128)
    Component_069 = models.CharField(verbose_name='成分069', blank=True, null=True, max_length=128)
    Component_070 = models.CharField(verbose_name='成分070', blank=True, null=True, max_length=128)
    Component_071 = models.CharField(verbose_name='成分071', blank=True, null=True, max_length=128)
    Component_072 = models.CharField(verbose_name='成分072', blank=True, null=True, max_length=128)
    Component_073 = models.CharField(verbose_name='成分073', blank=True, null=True, max_length=128)
    Component_074 = models.CharField(verbose_name='成分074', blank=True, null=True, max_length=128)
    Component_075 = models.CharField(verbose_name='成分075', blank=True, null=True, max_length=128)
    Component_076 = models.CharField(verbose_name='成分076', blank=True, null=True, max_length=128)
    Component_077 = models.CharField(verbose_name='成分077', blank=True, null=True, max_length=128)
    Component_078 = models.CharField(verbose_name='成分078', blank=True, null=True, max_length=128)
    Component_079 = models.CharField(verbose_name='成分079', blank=True, null=True, max_length=128)
    Component_080 = models.CharField(verbose_name='成分080', blank=True, null=True, max_length=128)
    Component_081 = models.CharField(verbose_name='成分081', blank=True, null=True, max_length=128)
    Component_082 = models.CharField(verbose_name='成分082', blank=True, null=True, max_length=128)
    Component_083 = models.CharField(verbose_name='成分083', blank=True, null=True, max_length=128)
    Component_084 = models.CharField(verbose_name='成分084', blank=True, null=True, max_length=128)
    Component_085 = models.CharField(verbose_name='成分085', blank=True, null=True, max_length=128)
    Component_086 = models.CharField(verbose_name='成分086', blank=True, null=True, max_length=128)
    Component_087 = models.CharField(verbose_name='成分087', blank=True, null=True, max_length=128)
    Component_088 = models.CharField(verbose_name='成分088', blank=True, null=True, max_length=128)
    Component_089 = models.CharField(verbose_name='成分089', blank=True, null=True, max_length=128)
    Component_090 = models.CharField(verbose_name='成分090', blank=True, null=True, max_length=128)
    Component_091 = models.CharField(verbose_name='成分091', blank=True, null=True, max_length=128)
    Component_092 = models.CharField(verbose_name='成分092', blank=True, null=True, max_length=128)
    Component_093 = models.CharField(verbose_name='成分093', blank=True, null=True, max_length=128)
    Component_094 = models.CharField(verbose_name='成分094', blank=True, null=True, max_length=128)
    Component_095 = models.CharField(verbose_name='成分095', blank=True, null=True, max_length=128)
    Component_096 = models.CharField(verbose_name='成分096', blank=True, null=True, max_length=128)
    Component_097 = models.CharField(verbose_name='成分097', blank=True, null=True, max_length=128)
    Component_098 = models.CharField(verbose_name='成分098', blank=True, null=True, max_length=128)
    Component_099 = models.CharField(verbose_name='成分099', blank=True, null=True, max_length=128)
    Component_100 = models.CharField(verbose_name='成分100', blank=True, null=True, max_length=128)
    # 登録日
    registered = models.DateField(verbose_name='登録日', blank=True, null=True, max_length=16)

    def __str__(self):
        return self.product



''' カテゴリテーブル '''
class Category(models.Model):
    # マスタId
    id = models.AutoField(primary_key=True)
    # カテゴリタイプ
    category_type = models.CharField(verbose_name='カテゴリタイプ', blank=True, null=True, max_length=32)
    # カテゴリId
    category_id = models.CharField(verbose_name='カテゴリId', blank=True, null=True, max_length=32)
    # カテゴリ名
    category = models.CharField(verbose_name='カテゴリ名', blank=True, null=True, max_length=128)
    # 並び順
    order = models.CharField(verbose_name='並び順', blank=True, null=True, max_length=8)
    # 登録日
    registered = models.DateField(verbose_name='登録日', blank=True, null=True, max_length=16)

    def __str__(self):
        return self.category
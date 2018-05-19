from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField


class Section(models.Model):
    class Meta:
        db_table = 'section'

    section_title = models.CharField(max_length=200)
    section_url = models.CharField(max_length=50)
    section_description = models.TextField()

    def __str__(self):
        return self.section_title


class Post(models.Model):
    class Meta:
        db_table = "Post"

    post_title = models.CharField("Заголовок", max_length=100)
    post_section = models.ForeignKey(Section, related_name="Категория", on_delete=models.CASCADE, )
    post_author = models.ForeignKey(User, related_name="Автор", on_delete=models.CASCADE, )
    post_date = models.DateTimeField('Дата публикации', default=timezone.now)
    # content = RichTextField("Ваша Заявка")
    post_content = models.TextField("Ваша Заявка")
    post_photo = models.ImageField("Фото", upload_to='photo', blank=True)
    post_status = models.IntegerField("Статус")
    post_visits = models.IntegerField("Количество Посещений", default=0)
    post_likes = models.IntegerField("Лайки", default=0)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        print(self.post_photo, self.post_content, self.post_section.id)
        if not self.post_photo:
            self.post_photo = 'category/{}.png'.format(self.post_section.id)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    # path = ArrayField(models.IntegerField())
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, )
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, )
    content = models.TextField('Комментарий')
    pub_date = models.DateTimeField('Дата комментария', default=timezone.now)

    def __str__(self):
        return self.content[0:200]

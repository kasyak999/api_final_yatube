from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        """Перевод модели"""

        verbose_name = 'группа'
        verbose_name_plural = 'Группы'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name='Группа'
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follow_User')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follow_following',)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['user', 'following'],
    #             name='unique_name_owner'
    #         )
    #     ]

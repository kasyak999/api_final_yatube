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
        User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        verbose_name='Изображение')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name='Группа'
    )

    class Meta:
        """Перевод модели"""
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ('pub_date',)
        default_related_name = 'posts'

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(
        verbose_name='Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        """Перевод модели"""
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ('created',)
        default_related_name = 'comments'

    def __str__(self):
        return self.text


class Follow(models.Model):
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='на кого подписан')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name='Подписчик')

    class Meta:
        """Перевод модели"""
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('user',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_name_owner'
            )
        ]

    def __str__(self):
        return f'Подписчик {self.user}'

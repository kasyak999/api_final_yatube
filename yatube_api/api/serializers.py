from rest_framework import serializers


from posts.models import Comment, Post, Group, Follow
from django.contrib.auth import get_user_model


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    pub_date = serializers.DateTimeField(read_only=True)
    group = serializers.SlugRelatedField(
        slug_field='id', queryset=Group.objects.all(),
        required=False)

    class Meta:
        fields = '__all__'
        model = Post

    #         "author": "kasyak",
    #         "pub_date": "2024-09-10T15:49:08.818816Z",
    #         "group": null,
    #         "text": "tgtgt",
    #         "image": null

    def get_comments(self, obj):
        return obj.comments.count()


    # pub_date = serializers.DateTimeField(read_only=True)
    # comments = serializers.SerializerMethodField(read_only=True)
    # group = serializers.SlugRelatedField(
    #     slug_field='title', read_only=True
    # )

    # class Meta:
    #     model = Post
    #     fields = '__all__'

    # def get_comments(self, obj):
    #     return obj.comments.count()
    


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('created', 'post')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Вы не можете подписаться на себя!')
        elif Follow.objects.filter(
            user=self.context['request'].user, following=value
        ).exists():
            raise serializers.ValidationError('Вы уже подписаны на него.')
        return value

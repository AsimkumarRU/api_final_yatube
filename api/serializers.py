from rest_framework.generics import get_object_or_404
from rest_framework import serializers

from .models import Comment, Post, Group, Follow, User



class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    def validate(self, data):
        user = get_object_or_404(User, username=data['following'].username)
        follow = Follow.objects.filter(
            user=self.context['request'].user,
            following=user).exists()
        if user == self.context['request'].user:
            raise serializers.ValidationError(
        "Вы не можете подписаться сами на себя")
        if follow is True:
            raise serializers.ValidationError(
        "Вы уже подписаны на этого пользователя")
        return data

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('id', 'user')

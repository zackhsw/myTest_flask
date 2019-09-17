class Message:
    def __init__(self, actor, target_data, object_data=None):
        self.actor = actor
        self.target_data = target_data
        self.object_data = object_data

    def actor(self):
        return self.actor

    def verb(self):
        pass  # 待重载

    def target(self):
        # 从target_data中得到target
        pass

    def object(self):
        # 从object_data中得到object
        pass

    def template(self):
        # 待重载
        return f"{self.actor}{self.verb}你的回答{self.target}"  # 使用了python的字符串内插语法

    def receiver(self):
        return self.target.followers

    def send(self):
        # redis处理
        pass


class UpMessage(Message):
    def verb(self):
        return "点赞了"


class FollowMessage(Message):
    def verb(self):
        return "关注了"


class StarMessage(Message):
    def verb(self):
        return "收藏了"


class AnswerUpMessage(UpMessage):
    def template(self):
        return f"{self.actor}{self.verb}你的回答{self.target}"


class CommentUpMessage(UpMessage):
    def template(self):
        return f"{self.actor}{self.verb}你的评论{self.target}"

class WechatMixin:
    def wechat_template(self):
        # 根据微信公众号的设置填充模版
        pass

    def send_wechat(self):
        # 发送给微信用户
        pass

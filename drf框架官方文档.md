### Tutorial 2: Requests and Responses

我们需要开始使用Web API的第一件事是提供一种将代码段实例序列化和反序列化为表示形式（如json）的方法。 我们可以通过声明与Django表单非常相似的序列化器来完成此操作。 在名为serializers.py的snippets目录中创建一个文件，并添加以下内容。

Serializer与ModelSerializer的区别：
ModelSerializer只是一种创建实例化的快捷方式，可以自动创建确定的字段，也就是自动“简单”实现create()和update()方法

主要感受： 与Django普通接口相比，Django接收一个Request，然后orm查询数据库，然后调用JsonParser返回而DRF框架相比在于，Django接收一个Request，orm调用，Serializer通过，然后再JsonParser。
总体相比，我们还需要继续查询究竟Serializer究竟是如何工作的，以及为什么要用Serializer



### Tutorial 3: Class-based Views

这篇根据标题来讲，应该是讲的CBV模式，上一篇讲的应该属于FBV模式

普通的我们可以继承APIviews

当然我们可以应用Mixins，继承Mixins中的方法，继承GenericAPIView ，很方便的一两行代码写出REST风格的接口
mixins中使用ListModelMixin、CreateModelMixin、GenericAPIView、RetrieveModelMixin、UpdateModelMixin、DestroyModelMixin方法

但我们可以通过更好的方式，也就是混合视图的方法来减少我们的的代码，如使用ListCreateAPIView代替同时继承ListModeMixin\CreateModelMixin\GenericAPIView，实际上用这种代码连业务逻辑都省了



### Tutorial 4: Authentication & Permissions

这篇讲的是权限认证，他就是说啊，不能让啥人都修改咱的REST接口，很简单的一章




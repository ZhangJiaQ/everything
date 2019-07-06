### Tutorial 2: Requests and Responses

我们需要开始使用Web API的第一件事是提供一种将代码段实例序列化和反序列化为表示形式（如json）的方法。 我们可以通过声明与Django表单非常相似的序列化器来完成此操作。 在名为serializers.py的snippets目录中创建一个文件，并添加以下内容。

Serializer与ModelSerializer的区别：
ModelSerializer只是一种创建实例化的快捷方式，可以自动创建确定的字段，也就是自动“简单”实现create()和update()方法

主要感受： 与Django普通接口相比，Django接收一个Request，然后orm查询数据库，然后调用JsonParser返回而DRF框架相比在于，Django接收一个Request，orm调用，Serializer通过，然后再JsonParser。
总体相比，我们还需要继续查询究竟Serializer究竟是如何工作的，以及为什么要用Serializer



### Tutorial 3: Class-based Views

这篇根据标题来讲，应该讲的CBV（Class by view）模式

普通的接口我们可以继承APIviews

当然我们可以通过继承Mixins中的对象，并且继承GenericAPIView，很方便的一两行代码写出REST风格的接口

mixins使用ListModelMixin\CreateModelMixin\GenericAPIView\RetrieveModelMixin\UpdateModelMixin\DestoryModelMixin对象，“重构”对象的list\create等方法

但我们可以通过更好的方式，也就是通过混合视图的方式来减少我们的代码，如使用ListCreateAPIview代替继承ListModelMixin\CreateModelMixin\GenericAPIView

各个View的区别

APIView

GenericAPIView

ViewSet

混合视图



### Tutorial 4: Authentication & Permissions

这篇讲的是权限管理

我们可以通过一种方式来对API进行权限管理

1. 在我们定义好的models.py增加对用户的外键
2.  在我们定义好的Serializer.py中增加权限管理，增加UserSerializer
3. 在views.py增加UserList与UserDetail方便登陆
4. 在Url中定义登陆url
5. 在之前定义好的view中的class增加perform_create
6. 在之前定义好的serializer的class中增加ReadOnlyField
7. 调用rest_framework的permission，加入之前view的class
8. 增加permission文件，创建IsOwenerOrReadOnly类，保证只有写入才需要权限认证
9. 将isOwenerOrReadOnly增加至之前view的permission中，做权限认证



### Tutorial 5: Relationships & Hyperlinked APIs

这篇指的是如何提高API的内聚性与可发现性

内聚性: 

可发现性： 即使是没有接口文档，我们可以通过在根目录设置返回各个项目的url来提高可发现性

1. 创建根目录下的api_root文件，返回Response以及key-value对，key为项目名，value为reverse(name, request, format=None)
2. 创建SnippetHighlight对象，用于返回HTML代码
3. 通过在serializers.py中，对我们各个项目的对象增加highlight属性，传入HyperlinkedIdentityField对象，则我们访问根目录的时候可以返回超链接。
4. 确保我们url.py文件中的URL已经被命名，方便api_root的查找
5. 在setting.py中增加分页



### Tutorial 6: ViewSets & Routers

这篇主要是将viewsets与routers类型的，应该是一种方便开发的方式

viewsets与普通view实际上相同，但不需要使用get/put的方式提供更新与添加操作

通常使用Router实例化一组viewsets

与之前的代码不同，比如我们在定义User view的时候定义了两个，一个位UserList，另一个为UserDetail，但我们可以通过viewsets定义一个类，实现之前两个类才能实现的方法。

完成后我们需要将viewsets绑定到url

在设置url的时候我们无需像以前那种方式自己在urlpartten中添加，而是采用router方式进行路由注册，减少代码

使用视图集的好处：

使用视图集可能是一个非常有用的抽象。 它有助于确保URL约定在您的API中保持一致，最大限度地减少您需要编写的代码量，并使您可以专注于API提供的交互和表示，而不是URL conf的细节。

这并不意味着它始终是正确的方法。 当使用基于类的视图而不是基于函数的视图时，需要考虑类似的一组权衡。 使用视图集不如单独构建视图那么明确。



### Tutorial 7: Schemas & client libraries

Schemas 是一个machine-readable的文档，描述了可用的API端点，它们的URL以及它们支持的操作。

Schemas可以是自动生成文档的有用工具，也可以用于驱动可以与API交互的动态客户端库。
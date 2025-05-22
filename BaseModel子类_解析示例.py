from langchain_core.pydantic_v1 import BaseModel, Field  # 导入 BaseModel, Field 类

# 自定义类
class Xiaohongshu(BaseModel):  # 自定义类，作为BaseModel类的子类(继承)
    # 创建 自定义类变量
    主_题: list[str] = Field(description="小红书的5个标题",min_items=5,max_items=5,)  # 自定义类变量。类型是list “列表类型”，而列表里面的元素是str “字符串类型”
    内_容: str = Field(description="小红书的正文内容")  # 自定义类变量: 类型名(可以用于指定字段的类型)。类型是 str “字符串类型”

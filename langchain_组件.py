from prompt_template_字符 import system_提示,user_提示       # 从文件 prompt_template_组件 导入 system_提示,user_提示（2个变量）
from BaseModel子类_解析示例 import Xiaohongshu               # 从文件 定义解析示例 导入 Xiaohongshu
from langchain.prompts import ChatPromptTemplate           # 旧版本（0.0.200 之前）
from langchain_openai import ChatOpenAI                    #  导入 聊天模型的类
from langchain.output_parsers import PydanticOutputParser  # 导入 Pydantic解析器 类
import os

# 自定义函数
def xiaohongshu_generator(api_key,主题,):
    # ---创建 提示模板 ChatPromptTemplate 对象---
    prompt_template = ChatPromptTemplate.from_messages([
        ("system",system_提示),  # 系统消息。设定模型的行为和回复语言。
        ("human", user_提示)     # 用户消息。用户提供需要翻译的文本。
    ])

    # ---创建 模型组件 ChatOpenAI对象(实例)---
    模型组件 = ChatOpenAI(
        model = "gemini-2.0-flash",
        api_key = api_key,
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/")

    # ---创建 解析器组件---
    pydantic_输出_解析器 =PydanticOutputParser(pydantic_object=Xiaohongshu)  # Pydantic输出解析器 对象

    # ---创建 链---
    chain = prompt_template | 模型组件 | pydantic_输出_解析器

    # ---链式调用---
    类_对象 =chain.invoke(
        {"parser_instructions": pydantic_输出_解析器.get_format_instructions(),  # 解析器_格式指令
         "theme": 主题}
    )
    return 类_对象

# 测试
# 结果 = xiaohongshu_generator("","宝宝")
# print(结果.主_题)
# print(结果.内_容)



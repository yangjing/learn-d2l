FROM python:3.9

WORKDIR /notebook

RUN mkdir /notebook && pip install --upgrade pip && pip install torch==1.12.1 torchvision==0.13.1 d2l==0.17.6 -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["jupyter", "notebook", "--allow-root", "--ip=0.0.0.0", "--port=8890"]


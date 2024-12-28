from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.charts import Bar
import webbrowser


class Visualizer:
    url_prefix = ("file:///C:/Users/Rossignol/Desktop/school/courses/"
                  "python/python-school/pyLab/design/data/visualizations/")
    name_prefix = "../data/visualizations/"
    BAR_CHARTS = 1
    PIE_CHARTS = 2

    def generate_bar_chart(self, x_data, y_data, filename):
        fullname = self.name_prefix + filename + ".html"
        path = url_prefix + filename + ".html"
        # 创建柱状图
        bar = Bar()
        bar.add_xaxis(x_data)
        bar.add_yaxis("单词出现数", y_data)

        # 配置图表
        bar.set_global_opts(
            title_opts=opts.TitleOpts(title="菜鸟教程技术出现数柱状图"),
            xaxis_opts=opts.AxisOpts(name="名称"),
            yaxis_opts=opts.AxisOpts(name="出现数"),
        )

        # 渲染图表
        bar.render(fullname)

        # 查看图表
        webbrowser.open(path)

    def generate_pie_chart(self, data, filename):
        fullname = self.name_prefix + filename + ".html"
        path = url_prefix + filename + ".html"
        # 创建饼状图
        pie = Pie()
        pie.add("", data)

        # 配置图表
        pie.set_global_opts(
            title_opts=opts.TitleOpts(title="菜鸟教程技术出现数饼状图"),
        )

        # 渲染图表
        pie.render(fullname)

        # 查看图表
        webbrowser.open(path)


if __name__ == "__main__":
    test = Visualizer()

    url_prefix = ("file:///C:/Users/Rossignol/Desktop/school/courses/"
                  "python/python-school/pyLab/design/data/visualizations/")
    # 准备数据
    x_data = ['一月', '二月', '三月', '四月', '五月']
    y_data = [10, 20, 15, 25, 30]
    data = [list(z) for z in zip(x_data, y_data)]
    data_dict = dict(zip(x_data, y_data))

    test.generate_bar_chart(x_data, y_data, "test1")
    test.generate_pie_chart(data, "test2")


from transformers import BartTokenizer, BartForConditionalGeneration, pipeline
import evaluate
from datasets import load_dataset


class AiSummary:
    url_prefix = '../data/extract/'
    output_prefix = '../data/summary/'

    def summary(self):
        # 加载预训练的BART模型和分词器
        model_name = "facebook/bart-large-cnn"  # 使用预训练的BART模型，适合文本概括
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)

        path = self.url_prefix + 'content.txt'
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()

        # 对文本进行分词和编码
        inputs = tokenizer(content, return_tensors="pt", max_length=1024, truncation=True, padding="longest")

        # 使用BART模型进行文本概括
        summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=50,
                                     length_penalty=2.0, num_beams=4, early_stopping=True)

        # 解码生成的id为文本
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        with open(self.output_prefix + 'test.txt', 'w', encoding='utf-8') as out:
            out.write(summary)

        print("\nSummarized Text:")
        print(summary)

        return summary

    def evaluate(self):
        # 加载数据集
        dataset = load_dataset("cnn_dailymail", "3.0.0", split="test")

        # 加载预训练的文本生成模型
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

        # 加载ROUGE评估器
        rouge = evaluate.load("rouge")

        # 获取参考摘要和生成的摘要
        references = dataset["highlights"][:5]  # 选择前5个参考摘要
        articles = dataset["article"][:5]  # 选择前5个文章

        # 使用模型生成摘要
        predictions = summarizer(articles, max_length=150, min_length=50, do_sample=False)

        # 计算ROUGE得分
        results = rouge.compute(predictions=[summary["summary_text"] for summary in predictions], references=references)

        print("ROUGE Scores:", results)


if __name__ == "__main__":
    test = AiSummary()
    test.summary()
    test.evaluate()

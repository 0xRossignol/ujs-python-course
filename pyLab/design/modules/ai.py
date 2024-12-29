from transformers import BartTokenizer, BartForConditionalGeneration
import evaluate


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

    def evaluate(self):
        # 加载ROUGE评估指标
        rouge = evaluate.load("rouge")
        # 读取生成的摘要和参考摘要
        generated_summary_path = self.output_prefix + 'test.txt'
        with open(generated_summary_path, 'r', encoding='utf-8') as f:
            generated_summary = f.read()
        # 参考摘要
        reference_summary_path = self.output_prefix + 'reference.txt'  # 参考文件路径
        with open(reference_summary_path, 'r', encoding='utf-8') as f:
            reference_summary = f.read()
        # 计算ROUGE分数
        results = rouge.compute(predictions=[generated_summary], references=[reference_summary])
        # 输出评估结果
        print("\nROUGE Scores:")
        print(results)


if __name__ == "__main__":
    test = AiSummary()
    test.summary()

const content = {
  zh: {
    tasks: {
      concept: { title: "概念科普", summary: "把陌生概念讲清楚，而不是写成方法学综述。", output: "概念定义、价值、基本操作、典型结果和常见误区", prompt: "Use $ai-knowledge-writing-skill to explain [topic] for [audience] in [length] Chinese characters. Define it plainly, explain why it matters, show the basic workflow and outputs, and keep limitations visible." },
      source: { title: "附件解读", summary: "先确认附件直接展示了什么，再写成新的读者结构。", output: "来源清单、事实/推断拆分、原创公众号文案", prompt: "Use $ai-knowledge-writing-skill to inspect [source], separate visible facts from inference and missing context, then write an original Chinese explainer for [audience] without copying its wording or order." },
      health: { title: "医学科普", summary: "用权威来源和适用边界处理高风险结论。", output: "证据受限的医学科普、来源说明和教育用途边界", prompt: "Use $ai-knowledge-writing-skill to write a public explainer about [medical topic]. Verify authoritative sources, state population and evidence limits, avoid individual diagnosis or treatment advice, and deliver [format]." },
      compare: { title: "产品比较", summary: "按同一维度比较，并把价格写成有日期的快照。", output: "团队、时间、形态、优势、短板、成本和场景比较", prompt: "Use $ai-knowledge-writing-skill to compare [products] as of [date]. Verify official sources, use equal dimensions, separate software and usage costs, and recommend by scenario rather than declaring one universal winner." },
      glossary: { title: "词汇解释", summary: "保留清单顺序，一词一句，并核对数量与重复项。", output: "完整、顺序一致、适合复制发布的词汇清单", prompt: "Use $ai-knowledge-writing-skill to verify and explain the [count] supplied terms in one plain sentence each. Preserve order, flag informal labels cautiously, detect duplicates, and validate the exact count." }
    },
    copied: "提示词已复制",
    failed: "浏览器未允许自动复制，请手动选择提示词。"
  },
  en: {
    tasks: {
      concept: { title: "Concept explainer", summary: "Explain an unfamiliar idea without turning it into a methods review.", output: "Definition, value, basic workflow, typical outputs, and misconceptions", prompt: "Use $ai-knowledge-writing-skill to explain [topic] for [audience] in [length]. Define it plainly, explain why it matters, show the basic workflow and outputs, and keep limitations visible." },
      source: { title: "Source interpretation", summary: "Identify what the attachment directly shows before creating a new reader structure.", output: "Source map, fact/inference split, and original public article", prompt: "Use $ai-knowledge-writing-skill to inspect [source], separate visible facts from inference and missing context, then write an original explainer for [audience] without copying its wording or order." },
      health: { title: "High-stakes explainer", summary: "Use authoritative evidence and scope boundaries for consequential claims.", output: "Evidence-bounded article, source notes, and educational-use boundary", prompt: "Use $ai-knowledge-writing-skill to write a public explainer about [high-stakes topic]. Verify authoritative sources, state population and evidence limits, avoid individualized advice, and deliver [format]." },
      compare: { title: "Product comparison", summary: "Use equal dimensions and date-sensitive cost snapshots.", output: "Owner, timeline, form, strengths, limits, cost model, and fit", prompt: "Use $ai-knowledge-writing-skill to compare [products] as of [date]. Verify official sources, use equal dimensions, separate software and usage costs, and recommend by scenario rather than declaring one universal winner." },
      glossary: { title: "Glossary", summary: "Preserve order, explain one item per sentence, and verify count and duplicates.", output: "Complete, ordered, publication-ready glossary", prompt: "Use $ai-knowledge-writing-skill to verify and explain the [count] supplied terms in one plain sentence each. Preserve order, flag informal labels cautiously, detect duplicates, and validate the exact count." }
    },
    copied: "Prompt copied",
    failed: "Automatic copy was blocked. Select the prompt manually."
  }
};

const language = document.documentElement.lang.startsWith("zh") ? "zh" : "en";
const labels = content[language];
const tabs = [...document.querySelectorAll("[data-task]")];
const title = document.querySelector("[data-panel-title]");
const summary = document.querySelector("[data-panel-summary]");
const output = document.querySelector("[data-panel-output]");
const prompt = document.querySelector("[data-panel-prompt]");
const status = document.querySelector("[data-copy-status]");

function selectTask(id) {
  const item = labels.tasks[id];
  tabs.forEach((tab) => {
    const active = tab.dataset.task === id;
    tab.classList.toggle("active", active);
    tab.setAttribute("aria-selected", String(active));
  });
  title.textContent = item.title;
  summary.textContent = item.summary;
  output.textContent = item.output;
  prompt.textContent = item.prompt;
}

tabs.forEach((tab) => tab.addEventListener("click", () => selectTask(tab.dataset.task)));
document.querySelector("[data-copy]").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(prompt.textContent);
    status.textContent = labels.copied;
  } catch {
    status.textContent = labels.failed;
  }
});

selectTask("concept");

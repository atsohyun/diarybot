## Chat with Your Diary

Diarybot (in Korean: '일기봇') is a messenger chatbot with which you can talk about your deepest feelings and thoughts about a trauma in the past.

### Motivation
In times of sorrow and even despair, we often turn to someone who'd listen to our stories. Telling stories helps, but it's also difficult not only because those stories are mostly quite private, but also a soundboard can only help so much. Hence we ask: what is a chatbot listens to your stories and follows up with you? Diarybot is a chatbot on [Kakao](www.kakao.com) that helps with user engagement in the self-reflection process upon recollecting past trauma. 

### Expressive Writing
The basic setup borrows heavily from [James W. Pennebaker](https://liberalarts.utexas.edu/psychology/faculty/pennebak)'s seminal work on expressive writing. Since the late 1990s, Dr. Pennebaker and his colleagues have conducted an extensive research on how writing about one's past trauma can lead to health benefits. The writing prompt is as follows:
```
In your writing, I would like you to really let go and explore your very deepest emotions and thoughts about the most traumatic experience in your entire life. You might tie this trauma to other parts of your life: your childhood, your relationships with others, including parents, lovers, friends, relatives, or other people important to you. You might link your writing to your future and who you would like to become in your future, or to who you have been, or who you are now. Not everyone has had a single trauma, but all of us have had major conflicts or stressors, and you can write about these as well. All your writing is confidential. There will be no sharing of content. Do not worry about form or style, spelling, punctuation, sentence structure, or grammar.
```

### Design
We built a chatbot that first delivers Pennebaker's expressive writing prompt, and upon what a user writes in response, follows up with a series of five questions that ask the user to detail the feelings surfaced from the writing, as well as review the relationship with a key person in the writing. We borrowed the questions from psychotherapy practice and [Naikan therapy](https://tricycle.org/magazine/naikan-therapy/). We had the chatbot refer to the most prevalent emotions in the writing and the key person. For more information about the technical details, please contact me. We built Diarybot on [kakao i open builder](i.kakao.com) platform. 

### Acknowledgement
* We are inspired by [many kind-hearted developers](https://lovit.github.io/nlp/2019/04/30/textrank/) online, and indebted to [their hard work](https://bab2min.tistory.com/570) for implementing the TextRank algorithm in Korean.
* Many thanks to [James W. Pennebaker](https://liberalarts.utexas.edu/psychology/faculty/pennebak) for his insightful comments and feedback!

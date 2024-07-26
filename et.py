from ast import literal_eval

df_post['PostMention'] = df_post['PostMention'].apply(lambda x: literal_eval(str(x)))

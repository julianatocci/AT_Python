def export_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Arquivo {filename} salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar {filename}:", e)

def export_json(df, filename):
    try:
        df.to_json(filename, orient="records", force_ascii=False, indent=4)
        print(f"Arquivo {filename} salvo com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar {filename}:", e)

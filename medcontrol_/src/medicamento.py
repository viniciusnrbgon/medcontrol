import requests

class MedicamentoService:
    @staticmethod
    def buscar_medicamento_por_nome(nome_medicamento: str) -> dict:
        """
        Busca informações de um medicamento na API pública da OpenFDA.
        """
        if not nome_medicamento:
            raise ValueError("O nome do medicamento não pode estar vazio.")

        url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{nome_medicamento}&limit=1"
        
        try:
            response = requests.get(url, timeout=10)
            
            if response.status_code == 404:
                raise Exception("Medicamento não encontrado na base de dados externa.")
            elif response.status_code != 200:
                raise Exception("Erro na comunicação com a API externa.")

            dados = response.json()
            resultado = dados['results'][0]

            return {
                "nome": resultado.get('openfda', {}).get('brand_name', [nome_medicamento])[0],
                "fabricante": resultado.get('openfda', {}).get('manufacturer_name', ['Desconhecido'])[0],
                "substancia_ativa": resultado.get('active_ingredient', ['Não informada'])[0],
                "finalidade": resultado.get('purpose', ['Não informada'])[0]
            }

        except requests.exceptions.RequestException as e:
            raise Exception(f"Falha de conexão com a API: {str(e)}")

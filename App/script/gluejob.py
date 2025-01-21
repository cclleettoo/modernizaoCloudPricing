import json
import logging

from libglueplataformacredito.dicionariodedados import DicionarioExecucao
from libglueplataformacredito.preparacaodedados import PreparacaoDeDados
from libglueplataformacredito.normalizacaodedados import NormalizacaoDeDados
from libglueplataformacredito.aplicacaoderegras import AplicacaoDeRegras
from libglueplataformacredito.qualidadededados import QualidadeDeDados

from libglueplataformacredito.utils import (
    configura_spark, debug_log
)

def main():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    logging.info("[INÍCIO DE EXECUÇÃO]")
    glue_context, spark = configura_spark()

    logging.info("Etapa: Dicionário de Execução")
    config = DicionarioExecucao()

    logging.info("Etapa: Preparação de Dados")
    preparacao_de_dados = PreparacaoDeDados(config, glue_context, spark)
    preparacao_de_dados.prepara_dados()

    logging.info("Etapa: Normalização de Dados")
    normalizacao_de_dados = NormalizacaoDeDados(config, glue_context, spark)
    normalizacao_de_dados.normaliza_dados()

    logging.info("Etapa: Aplicação de Regras")
    aplicacao_de_regras = AplicacaoDeRegras(config, glue_context, spark)
    aplicacao_de_regras.aplica_regras()

    logging.info("Etapa: Qualidade de Dados")
    qualidade_de_dados = QualidadeDeDados(config, glue_context, spark)
    qualidade_de_dados.qualidade_de_dados()

    if config.debug_mode:
        debug_log(config)

    if config.status_debug_performance:
        json_tempo_performance = json.dumps(config.tempo_debug_performance)
        logging.info(f'tempo_performance: {json_tempo_performance}')

    logging.info("[FIM DA EXECUÇÃO]")

if __name__ == "__main__":
    main()
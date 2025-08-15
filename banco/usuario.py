#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo de gerenciamento de usuários do sistema bancário.

Este módulo contém a classe Usuario que representa um usuário do sistema bancário,
com suas informações pessoais e métodos para gerenciar sua conta.
"""

from datetime import datetime


class Usuario:
    """
    Classe que representa um usuário do sistema bancário.
    
    Esta classe gerencia as informações do usuário e as operações relacionadas
    à sua conta bancária, como depósitos, saques e consulta de saldo.
    
    Parameters
    ----------
    nome : str
        Nome completo do usuário.
    saldo_inicial : float, optional
        Saldo inicial da conta do usuário (default é 0.0).
    
    Attributes
    ----------
    nome : str
        Nome completo do usuário.
    _saldo : float
        Saldo atual da conta (atributo privado).
    _historico : list
        Lista de transações realizadas pelo usuário.
    data_cadastro : datetime
        Data e hora de cadastro do usuário.
    
    Examples
    --------
    >>> usuario = Usuario("João Silva", 1000.0)
    >>> usuario.depositar(500.0)
    >>> usuario.sacar(200.0)
    >>> usuario.consultar_saldo()
    1300.0
    """
    
    def __init__(self, nome, saldo_inicial=0.0):
        """
        Inicializa um novo usuário com nome e saldo inicial.
        
        Parameters
        ----------
        nome : str
            Nome completo do usuário.
        saldo_inicial : float, optional
            Saldo inicial da conta do usuário (default é 0.0).
        """
        self.nome = nome
        self._saldo = float(saldo_inicial)
        self._historico = []
        self.data_cadastro = datetime.now()
        
        # Registra a transação inicial se houver saldo inicial
        if saldo_inicial > 0:
            self._registrar_transacao("Saldo inicial", saldo_inicial)
    
    def depositar(self, valor):
        """
        Realiza um depósito na conta do usuário.
        
        Parameters
        ----------
        valor : float
            Valor a ser depositado.
            
        Returns
        -------
        bool
            True se o depósito foi realizado com sucesso, False caso contrário.
            
        Raises
        ------
        ValueError
            Se o valor for negativo ou zero.
        """
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        
        self._saldo += valor
        self._registrar_transacao("Depósito", valor)
        return True
    
    def sacar(self, valor):
        """
        Realiza um saque na conta do usuário.
        
        Parameters
        ----------
        valor : float
            Valor a ser sacado.
            
        Returns
        -------
        bool
            True se o saque foi realizado com sucesso, False caso contrário.
            
        Raises
        ------
        ValueError
            Se o valor for negativo, zero ou maior que o saldo disponível.
        """
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        
        self._saldo -= valor
        self._registrar_transacao("Saque", -valor)
        return True
    
    def consultar_saldo(self):
        """
        Consulta o saldo atual da conta.
        
        Returns
        -------
        float
            Saldo atual da conta.
        """
        return self._saldo
    
    def _registrar_transacao(self, tipo, valor):
        """
        Registra uma transação no histórico do usuário.
        
        Parameters
        ----------
        tipo : str
            Tipo da transação (Depósito, Saque, etc).
        valor : float
            Valor da transação.
        """
        transacao = {
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now()
        }
        self._historico.append(transacao)
    
    def obter_historico(self):
        """
        Obtém o histórico de transações do usuário.
        
        Returns
        -------
        list
            Lista de dicionários contendo as transações realizadas.
        """
        return self._historico
    
    def __str__(self):
        """
        Retorna uma representação em string do usuário.
        
        Returns
        -------
        str
            Representação em string do usuário.
        """
        return f"Usuário: {self.nome}, Saldo: R$ {self._saldo:.2f}"
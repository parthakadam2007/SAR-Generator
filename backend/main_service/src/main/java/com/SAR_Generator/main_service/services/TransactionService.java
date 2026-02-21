package com.SAR_Generator.main_service.services;

import java.util.List;
import java.util.UUID;

import com.SAR_Generator.main_service.dto.TransactionDTO;

public interface TransactionService {
    public List<TransactionDTO> getByCaseId(UUID caseId );
}

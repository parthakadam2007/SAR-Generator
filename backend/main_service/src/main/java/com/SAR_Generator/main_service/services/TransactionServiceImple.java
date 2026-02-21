package com.SAR_Generator.main_service.services;

import com.SAR_Generator.main_service.dto.TransactionDTO;
import com.SAR_Generator.main_service.mapper.TransactionMapper;
import com.SAR_Generator.main_service.models.Transaction;
import com.SAR_Generator.main_service.repository.TransactionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class TransactionServiceImple implements TransactionService {

    private final TransactionRepository transactionRepository;


    private final TransactionMapper transactionMapper;

    @Override
    public List<TransactionDTO> getByCaseId(UUID caseId) {

        List<Transaction> transactions = transactionRepository.findByCaseEntity_Id(caseId);

        return transactionRepository
                .findByCaseEntity_Id(caseId)
                .stream()
                .map(TransactionMapper::toDTO) // ✅ Correct
                .toList();
    }
}

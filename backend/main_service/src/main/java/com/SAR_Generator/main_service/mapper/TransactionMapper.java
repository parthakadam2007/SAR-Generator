package com.SAR_Generator.main_service.mapper;


import com.SAR_Generator.main_service.dto.TransactionDTO;
import com.SAR_Generator.main_service.models.Case;
import com.SAR_Generator.main_service.models.Transaction;
import org.springframework.stereotype.Component;

import java.util.UUID;

@Component
public class TransactionMapper {

    // Entity → DTO
    public static TransactionDTO toDTO(Transaction transaction) {

        if (transaction == null) {
            return null;
        }

        return TransactionDTO.builder()
                .id(transaction.getId())
                .caseId(
                        transaction.getCaseEntity() != null
                                ?  UUID.fromString(transaction.getCaseEntity().getCaseId())
                                : null
                )
                .txId(transaction.getTxId())
                .timestamp(transaction.getTimestamp())
                .fromAccountMasked(transaction.getFromAccount())
                .toAccountMasked(transaction.getToAccount())
                .amount(transaction.getAmount())
                .currency(transaction.getCurrency())
                .channel(transaction.getChannel())
                .country(transaction.getCountry())
                .build();
    }


    // DTO → Entity
    public static Transaction toEntity(TransactionDTO dto, Case caseEntity) {

        if (dto == null) {
            return null;
        }

        return Transaction.builder()
                .id(dto.getId())
                .caseEntity(caseEntity) // must be loaded from DB
                .txId(dto.getTxId())
                .timestamp(dto.getTimestamp())
                .fromAccount(dto.getFromAccountMasked())
                .toAccount(dto.getToAccountMasked())
                .amount(dto.getAmount())
                .currency(dto.getCurrency())
                .channel(dto.getChannel())
                .country(dto.getCountry())
                .build();
    }
}
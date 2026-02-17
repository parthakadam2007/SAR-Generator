package com.SAR_Generator.main_service.repository;


import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.SAR_Generator.main_service.models.Transaction;

import java.math.BigDecimal;
import java.time.OffsetDateTime;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface TransactionRepository
        extends JpaRepository<Transaction, UUID> {

    // 🔍 Find transactions by Case ID
    List<Transaction> findByCaseEntity_Id(UUID caseId);

    // 🔍 Find by Transaction ID
    Optional<Transaction> findByTxId(String txId);

    // 🔍 Transactions in time range (AML analysis)
    List<Transaction> findByTimestampBetween(
            OffsetDateTime start,
            OffsetDateTime end
    );

    // 🔍 High-value transactions (risk detection)
    List<Transaction> findByAmountGreaterThan(BigDecimal amount);

    // 🔍 Transactions by account
    List<Transaction> findByFromAccountOrToAccount(
            String fromAccount,
            String toAccount
    );

    // 📄 Paginated by case
    Page<Transaction> findByCaseEntity_Id(UUID caseId, Pageable pageable);

    // 🚀 Fetch transaction + case
    @Query("""
        SELECT t FROM Transaction t
        JOIN FETCH t.caseEntity
        WHERE t.id = :id
    """)
    Optional<Transaction> findWithCase(UUID id);
}
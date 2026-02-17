package com.SAR_Generator.main_service.repository;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.SAR_Generator.main_service.models.AccountProfile;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface AccountProfileRepository
        extends JpaRepository<com.SAR_Generator.main_service.models.AccountProfile, UUID> {

    // 🔍 Find all account profiles by case ID
    List<com.SAR_Generator.main_service.models.AccountProfile> findByCaseEntity_Id(UUID caseId);

    // 🔍 Find account by account number
    Optional<AccountProfile> findByAccountNumber(String accountNumber);

    // 🔍 Find accounts by account type
    List<AccountProfile> findByAccountType(String accountType);

}
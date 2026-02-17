package com.SAR_Generator.main_service.repository;

import com.SAR_Generator.main_service.models.CustomerKyc;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CustomerKycRepository extends JpaRepository<CustomerKyc, UUID> {

    List<CustomerKyc> findByCaseEntity_Id(UUID caseId);

    Optional<CustomerKyc> findByCustomerId(String customerId);
}
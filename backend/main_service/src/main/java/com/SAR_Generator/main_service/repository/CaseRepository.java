package com.SAR_Generator.main_service.repository;

import java.util.Optional;
import java.util.UUID;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.SAR_Generator.main_service.models.Case;

@Repository
public interface CaseRepository extends JpaRepository<Case, UUID> {

    Optional<Case> findByCaseId(String caseId);

}

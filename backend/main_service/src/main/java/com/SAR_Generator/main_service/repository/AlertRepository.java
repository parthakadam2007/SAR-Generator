package com.SAR_Generator.main_service.repository;

import com.SAR_Generator.main_service.models.Alert;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Repository
public interface AlertRepository
        extends JpaRepository<Alert, UUID> {

    // 🔍 Find alerts by Case ID
    List<Alert> findByCaseEntity_Id(UUID caseId);

    // 🔍 Find alerts by severity (uses indexed column)
    List<Alert> findBySeverity(String severity);

    // 🔍 Find alert by alert ID
    Optional<Alert> findByAlertId(String alertId);

    // 📄 Paginated alerts by case
    Page<Alert> findByCaseEntity_Id(UUID caseId, Pageable pageable);

    // 🚀 Fetch alert with case (avoid LazyInitializationException)
    @Query("""
        SELECT a FROM Alert a
        JOIN FETCH a.caseEntity
        WHERE a.id = :id
    """)
    Optional<Alert> findWithCase(UUID id);
}
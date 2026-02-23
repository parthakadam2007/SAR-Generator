// package com.SAR_Generator.main_service.models;

// import com.SAR_Generator.main_service.repository.CaseAnalysis;
// import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
// import jakarta.persistence.*;
// import lombok.*;

// import java.util.UUID;

// @Entity
// @Table(name = "risk_breakdown")
// @JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
// @Getter
// @Setter
// @NoArgsConstructor
// @AllArgsConstructor
// @Builder
// public class RiskBreakdown {

//     @Id
//     @GeneratedValue
//     @Column(columnDefinition = "UUID")
//     private UUID id;

//     // Many RiskBreakdowns → One CaseAnalysis
//     @ManyToOne(fetch = FetchType.LAZY)
//     @JoinColumn(name = "analysis_id", nullable = false)
//     private CaseAnalysis caseAnalysis;

//     @Column(name = "customer_risk")
//     private Integer customerRisk;

//     @Column(name = "alert_risk")
//     private Integer alertRisk;

//     @Column(name = "geographic_risk")
//     private Integer geographicRisk;

//     @Column(name = "pattern_risk")
//     private Integer patternRisk;

//     @Column(name = "transaction_risk")
//     private Integer transactionRisk;
// }
package com.SAR_Generator.main_service.security;


import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.MalformedJwtException;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

@Component
public class JWTAuthenticationFilter extends OncePerRequestFilter {

    private static final Logger logger = LoggerFactory.getLogger(JWTAuthenticationFilter.class);

    @Autowired
    private JWTHelper jwtHelper;

    @Autowired
    private UserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

//         String path = request.getRequestURI();
//         if (path.matches("^/(api/auth/customer(/.*)?|)$")) {
//     filterChain.doFilter(request, response);
//     return;
// }

        // ✅ Skip JWT validation for public routes
        // if (path.equals("/") || path.startsWith("/api/auth/customer/")) {
        //     logger.debug("Skipping JWT filter for public route: {}", path);
        //     System.out.println("Skipping JWT filter for public route: " + path);    
        //     filterChain.doFilter(request, response);
        //     return;
        // }

        String requestHeader = request.getHeader("Authorization");
        logger.debug("Header: {}", requestHeader);
        System.out.println("Header:" + requestHeader);

        String username = null;
        String token = null;

        // ✅ Check header properly
        if (requestHeader != null && requestHeader.startsWith("Bearer ")) {
            token = requestHeader.substring(7);
            try {
                username = this.jwtHelper.getUsernameFromToken(token);
            } catch (IllegalArgumentException e) {
                logger.warn("Illegal argument while fetching username from token", e);
                filterChain.doFilter(request, response);
                return;
            } catch (ExpiredJwtException e) {
                logger.warn("JWT token is expired", e);
                filterChain.doFilter(request, response);
                return;
            } catch (MalformedJwtException e) {
                logger.warn("Invalid JWT token format", e);
                filterChain.doFilter(request, response);
                return;
            } catch (Exception e) {
                logger.error("Unexpected JWT error", e);
                filterChain.doFilter(request, response);
                return;
            }
        } else {
            logger.debug("No Bearer token found in header");
        }

        // ✅ Validate and set authentication
        if (username != null && SecurityContextHolder.getContext().getAuthentication() == null) {
            UserDetails userDetails = this.userDetailsService.loadUserByUsername(username);
            if (jwtHelper.validateToken(token, userDetails)) {
                UsernamePasswordAuthenticationToken authentication =
                        new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                authentication.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(authentication);
                logger.debug("User '{}' authenticated successfully", userDetails);
                System.out.println("User '" + username + "' authenticated successfully with context: " + SecurityContextHolder.getContext());
            } else {
                logger.warn("authenticated successfully with contextfor user: {}", username);
                response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
                response.setContentType("application/json");
                response.getWriter().write("{\"error\": \"Invalid token\"}");
                return;

            }
        }

        filterChain.doFilter(request, response);
    }
}

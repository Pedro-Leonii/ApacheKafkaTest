MSGS: list[str] = [
    "Application context initialized successfully.",
    "User 'testuser' logged in successfully.",
    "Processing new order with ID: O-456789.",
    "Deprecated API endpoint accessed. Please update your client.",
    "Attempting to connect to external payment service...",
    "Failed to connect to database. Check connection settings and credentials.",
    "Request payload received: {userId\":\"123\", \"action\":\"purchase\"}",
    "User 'guest' tried to access admin page without proper permissions.",
    "Could not process payment for order 'O-456789'. Reason: Payment gateway not responding.",
    "Scheduled daily report generation task completed successfully."
]

CLSES: list[str]  = [
    "org.apache.catalina.startup.Catalina",
    "org.apache.coyote.http11.Http11Processor",
    "org.apache.catalina.core.StandardService",
    "org.springframework.web.servlet.DispatcherServlet",
    "org.springframework.web.bind.annotation.RequestMapping",
    "org.springframework.jdbc.core.JdbcTemplate",
    "com.zaxxer.hikari.pool.HikariPool",
    "org.slf4j.LoggerFactory",
    "com.example.controller.ProductController",
    "com.example.service.UserService",
    "com.example.repository.OrderRepository"
]

THREADS: list[str] = [
    "main",
    "http-nio-8080",
    "http-nio-8080-exec-1",
    "http-nio-8080-exec-2",
    "HikariPool-1-ConnectionCreation",
    "task-scheduler-1",
    "Async-Task-Thread",
    "File-I/O-Thread",
    "thread-pool-executor-1"
]

URLS: list[str] = [
    "/homepage.html",
    "/user/profile.jsp",
    "/products/listing?category=electronics",
    "/products/item?id=P_12345",
    "/api/v1/user/101/data",
    "/checkout/cart.html",
    "/checkout/complete.jsp",
    "/images/logo.png",
    "/css/main.css",
    "/js/app.js",
    "/contact-us.html",
    "/login.html",
    "/logout"
]

USERS: list[str] = [
    "user123",
    "john.doe",
    "alice_smith",
    "guest_user",
    "admin",
    "pippo_baudo",
    "jane.doe",
    "guest",
    "giorgio.rossi",
    "mario_bianchi",
    None
]

STATUS_CODES: list[int] = [
    200,   
    301,  
    302,  
    400, 
    401,  
    403,  
    404,  
    500,  
    503   
]

USER_AGENTS: list[str] = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 15; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.5; rv:129.0) Gecko/20100101 Firefox/129.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Mozilla/5.0 (Android 14; Mobile; rv:128.0) Gecko/128.0 Firefox/128.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/128.0.2739.54 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36 Edg/128.0.2739.54",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36 OPR/114.0.5272.61",
    "Mozilla/5.0 (Linux; Android 14; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Mobile Safari/537.36 OPR/114.0.5272.61",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36 Brave/128.0.6613.120",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36 Brave/128.0.6613.120"
]

SEVERITY = [
    "INFO",
    "DEBUG",
    "WARNING",
    "ERROR"
]

METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "HEAD",
    "CONNECT",
    "OPTIONS",
    "TRACE",
    "PATCH"
]
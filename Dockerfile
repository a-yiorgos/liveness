# Use a slim Python image for a smaller footprint
FROM python:3.12-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8081

WORKDIR /app

# Create a non-privileged system user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Copy and install dependencies first to leverage Docker layer caching
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application source code with correct ownership
COPY --chown=appuser:appuser app.py .

# Switch to the non-privileged user for security
USER appuser

# Expose the port
EXPOSE 8081

# Optional: Add a container health check (update the endpoint if needed)
# HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
#   CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8081/health').read()" || exit 1

# Use split ENTRYPOINT and CMD for maximum flexibility
ENTRYPOINT ["python"]
CMD ["app.py"]

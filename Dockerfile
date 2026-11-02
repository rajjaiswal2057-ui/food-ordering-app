FROM python:3.12-slim
WORKDIR /app
COPY menu.py cart.py order.py calculate_total.py app.py ./
EXPOSE 5000
CMD ["python", "app.py"]

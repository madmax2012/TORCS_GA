figure();
while true
    subplot(1,1,1)
    results = csvread('test/run_1.csv');
    h1 = plot(results(:,3:4));
            set(h1,'LineStyle','--');
            title ('Fitness (max and mean)')
            xlabel('Generations');ylabel('Fitness');
    %hold on;
    pause(1.00);
end
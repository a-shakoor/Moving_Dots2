function [] = graphgazePsychopy()

gscommand = '/usr/local/Cellar/ghostscript/9.53.3/bin/gs';
gsfontpath = '/usr/local/Cellar/ghostscript/9.53.3/share/ghostscript/fonts';
gslibpath = '/usr/local/Cellar/ghostscript/9.53.3/lib';

sgfOrder = 3;
sgfFramelen = 5;

distanceToScreen = 57; %cm

%% Event Time CSV Indicies
trial = 1;
pupilTimestamp= 20;
psychopyTimestamp = 21;
cohOnPsychopy = 4;		
smoothPursuitStartPsychopy = 11;	
smoothPursuitStopPsychopy = 12;
response = 15;
pursuit_leftRight = 18;

%% Gaze Positions CSV Indicies
% updated for psychopy
conf_ind = 3;
gazetime_ind = 1;
posx_norm_ind = 4;
posy_norm_ind = 5;
posx_gaze3d_ind = 7;

gazefilepath = '~/Downloads/Moving_Dots-master/Results/Justin/gaze_positions.csv';
eventtimesfilepath = '~/Downloads/Moving_Dots-master/Results/Justin/justincombined_testDots_2020_Dec_11_1040.csv';
rawfile = readmatrix(gazefilepath); % Offsets to start at 2nd row (after headers)
eventtimes = readmatrix(eventtimesfilepath);


%% Filter Confidence above certain level
rawfile = rawfile(rawfile(:,conf_ind) > 0.5, :);

%% Throw out first X trials
firstValidTrial = 1;
eventtimes = eventtimes(eventtimes(:, 1) >= firstValidTrial, :);

%% Run through each Trial
clf
hold off
hold on
trialsWithoutPupil = zeros(1, 1);
for thistrial = 1:length(eventtimes(:,trial))
    tiledlayout(2,1)
    %% Filter both csv's to just the trial time ranges
    
    % First make sure there's a pupil start time
    thisTrialRow = eventtimes(thistrial,:)   
    trialNumber = thisTrialRow(1);
    if thisTrialRow(pupilTimestamp) == -1
        disp("----------------------------------------------------------------------------")
        disp("----------------------------------------------------------------------------")
        disp("WARNING: Pupil Data could not be recorded for trial number: " + trialNumber)
        disp("----------------------------------------------------------------------------")
        disp("----------------------------------------------------------------------------")
        trialsWithoutPupil(length(trialsWithoutPupil)+1) = trialNumber;
        continue
    end

    % Convert psychopy times to gaze times to find smooth pursuit gaze starttime
    smoothPursuitStartPupil = ...
        thisTrialRow(pupilTimestamp) - thisTrialRow(psychopyTimestamp)...
        + thisTrialRow(smoothPursuitStartPsychopy)
    % Add duration to smooth pursuit gaze starttime to find smooth pursuit gaze stoptime
    smoothPursuitStopPupil = ...
        (thisTrialRow(smoothPursuitStopPsychopy) - thisTrialRow(smoothPursuitStartPsychopy)) ...
        + smoothPursuitStartPupil;
    trialGaze = rawfile(rawfile(:,gazetime_ind) > smoothPursuitStartPupil, :);             
    trialGaze = trialGaze(trialGaze(:,gazetime_ind) < smoothPursuitStopPupil, :);

    if isempty(trialGaze)
        disp("----------------------------------------------------------------------------")
        disp("----------------------------------------------------------------------------")
        disp("WARNING: Pupil Data could not be recorded for trial number: " + trialNumber)
        disp("----------------------------------------------------------------------------")
        disp("----------------------------------------------------------------------------")
        trialsWithoutPupil(length(trialsWithoutPupil)+1) = trialNumber;
        continue
    end
    %% Throw out extraneous columns
    %trialGaze = trialGaze(:, 1:9);
    
    %% Set variables to plot
    disp("-----------------------------------------")
    disp("trial number: " + trialNumber)
    disp("smoothPursuitStartPsychopy: " + thisTrialRow(smoothPursuitStartPsychopy))
    disp("psychopyTimestamp: " + thisTrialRow(psychopyTimestamp))
    disp("pupilTimeStamp: " + thisTrialRow(pupilTimestamp))
    disp("smoothPursuitStartPupil: " + smoothPursuitStartPupil)
    disp("trial gaze length: " + length(trialGaze))
    x_gaze3d = trialGaze(:, posx_gaze3d_ind);
    disp("x gaze length: " + length(x_gaze3d))
    x_norm = trialGaze(:, posx_norm_ind);
    t = trialGaze(:, gazetime_ind) - trialGaze(1,gazetime_ind); % set first frame to t = 0;
    disp("t length: " + length(t))

    
    if length(x_gaze3d) < sgfFramelen
        disp("----------------------------------------------------------------------------")
        disp("----------------------------------------------------------------------------")
        disp("WARNING: Not enough data for trial number: " + trialNumber)
        disp("Only " + length(x_gaze3d) + " observations while frame length is " + sgfFramelen)
        disp("----------------------------------------------------------------------------")
        disp("----------------------------------------------------------------------------")
        trialsWithoutPupil(length(trialsWithoutPupil)+1) = trialNumber;
        continue
    end
    
    
    %% Transform x to degrees
    % formula angle = arccos((p1 dot p2) / (norm(p1) * norm(p2))
    % No actually, angle = arctan(dx / distance to screen)
    x_gaze3d_ang = zeros(length(x_gaze3d), 1);
    for i = 1:length(x_gaze3d)
       x_gaze3d_ang(i) = x_gaze3d(i) / 10; % mm to cm
       x_gaze3d_ang(i) = x_gaze3d_ang(i) - x_gaze3d_ang(1); % make each one relative to start
       x_gaze3d_ang(i) = atand(x_gaze3d_ang(i) / distanceToScreen);
    end
    disp("x gaze ang length: " + length(x_gaze3d_ang))

    t
    x_gaze3d_ang
    

    %% Plot Filtering and Velocity
    %   Use sgolay to smooth a noisy sinusoid and find its first three
    %   derivatives via a fifth order polynomial and a frame length of
    %   25 samples.
    hold on

    
    % Raw Position 
    nexttile
    plot(t, x_gaze3d_ang, '-o','MarkerIndices',1:length(x_gaze3d_ang));
    ylabel('Position (deg)');
    xlabel('Time (s)');
    
    % MATLAB Filtering (not accurate enough when differentiated. weird
%     % activity on the tails
%     
%     %[b,g] = sgolay(sgfOrder,sgfFramelen);
%     %position = conv(x_gaze3d_ang, factorial(0) * g(:,0+1), 'same');
%     %velocity = conv(x_gaze3d_ang, factorial(1) * g(:,1+1) / -.007, 'same');
%     
%     nexttile
%     yyaxis left
%     plot(t, x_gaze3d_ang, '-o','MarkerIndices',1:length(x_gaze3d_ang));
%     ylabel('Position (deg)');
%     yyaxis right
%     plot(t, velocity, '-o','MarkerIndices',1:length(t))
%     ylabel('Velocity (deg/s)');
%     legend('MATLAB Filtered Position', 'MATLAB Filtered Velocity', ...
%         'Location', 'southoutside');
%     title(append("Filtered Position/Velocity: Trial ", num2str(trialNumber), " (MATLAB)"));
       
    
   % External Filtering
    position_ext = abs(savitzkyGolayFilt(x_gaze3d_ang, sgfOrder, 0, sgfFramelen));
    velocity_ext = abs(savitzkyGolayFilt(x_gaze3d_ang, sgfOrder, 1, sgfFramelen) / -.007);
    
    nexttile
    
    
    yyaxis left
    %plot(t, x_gaze3d_ang, '-o','MarkerIndices',1:length(x_gaze3d_ang));
    plot(t, position_ext, '-o','MarkerIndices',1:length(t))
    ylabel('Position (deg)');
    
    
    yyaxis right
    plot(t, velocity_ext, '-o','MarkerIndices',1:length(t))
    ylabel('Velocity (deg/s)');
    
    xlabel('Time (s)');


%     %% Raw Plot Position
%     hold on
%     nexttile
%     plot(t, x_gaze3d_ang, '-o','MarkerIndices',1:length(x_gaze3d_ang));
%     ylabel('Position (deg)');
%     xlabel('Time (s)');
%     %sgf = sgolayfilt(t, sgfOrder, sgfFramelen);
%     %plot(t, sgf, '-o','MarkerIndices',1:length(y))
%     title("Raw Position Data (For Reference)");

    % Plot actual moving dot position
    hold on
    dotSpeed = 10;
    dir = thisTrialRow(pursuit_leftRight);
    %if(dir == 180) 
    %    dotSpeed = dotSpeed * -1 
    %end
    dotT = linspace(0,1);
    dotX = dotSpeed * dotT
    yyaxis left
    plot(dotT,dotX)
    
    %% Figure Options
    legend('Filtered Position', 'Actual Dot Position', 'Filtered Velocity', ...
    'Location', 'southoutside');
    title(append("Filtered Position/Velocity: Trial ", num2str(trialNumber)));

%  
%     x0=50;
%     y0=50;
%     width=600*1.3;
%     height=550*1.5;
%     set(gcf,'position',[x0,y0,width,height])

   print('~/Downloads/Moving_Dots-master/Results/Justin/PositionVelocityByTrialWithActualDotPosition.ps', ...
       '-dpsc', '-append', '-fillpage');           
   hold off
   clf    
end %%% for 


%%
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
disp("FINAL REPORT:")
disp("Number of Trials Initially Recorded: " + length(eventtimes(:,trial)))
disp("Analysis Started From Trial: " + firstValidTrial)
disp("Trials for which Pupil Data could not be Recorded: " + trialsWithoutPupil)
totalAnalyzed = length(eventtimes(:,trial)) - (firstValidTrial - 1) - trialsWithoutPupil;
disp("Total Number Trials Analyzed: " + totalAnalyzed)
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
disp("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

%ps2pdf('psfile','~/Downloads/Moving_Dots-master/Results/Justin/PositionVelocityByTrial.ps', ...
%       'pdffile', '~/Downloads/Moving_Dots-master/Results/Justin/PositionVelocityByTrial.pdf', ...
%      'gscommand', gscommand, 'gsfontpath', gsfontpath, 'gslibpath', gslibpath);


end

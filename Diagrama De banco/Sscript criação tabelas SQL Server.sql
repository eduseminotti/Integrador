USE [PortalDigital]
GO

/****** Object:  Table [dbo].[Users]    Script Date: 18/10/2019 19:38:46 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Users](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[Nome] [varchar](250) NOT NULL,
	[UserName] [varchar](250) NOT NULL,
	[Password] [varchar](250) NOT NULL,
	[tipo] [bigint] NOT NULL,
	[email] [varchar](250) NOT NULL,
	[Phone] [varchar](15) NULL,
 CONSTRAINT [PK_User] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


USE PortalDigital
GO

/****** Object:  Table [dbo].[Post]    Script Date: 18/10/2019 19:39:45 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Post](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[Titulo] [varchar](100) NOT NULL,
	[Conteudo] [varchar](max) NULL,
	[DataInicial] [date] NOT NULL,
	[DataFinal] [date] NOT NULL,
	[Tipo] [int] NOT NULL,
	[Status] [int] NOT NULL,
	[UserPostId] [bigint] NOT NULL,
	[insertdate] [datetime] NOT NULL CONSTRAINT [DF_Post_insertdate]  DEFAULT (getdate()),
 CONSTRAINT [PK_Post] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO

ALTER TABLE [dbo].[Post]  WITH CHECK ADD  CONSTRAINT [FK_Post_Post] FOREIGN KEY([UserPostId])
REFERENCES [dbo].[Users] ([id])
GO

ALTER TABLE [dbo].[Post] CHECK CONSTRAINT [FK_Post_Post]
GO




USE PortalDigital
GO

/****** Object:  Table [dbo].[Imagens]    Script Date: 18/10/2019 19:39:59 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Imagens](
	[Id] [bigint] IDENTITY(1,1) NOT NULL,
	[Image] [text] NOT NULL,
	[Insertdate] [datetime] NOT NULL,
	[Post_ID] [bigint] NOT NULL,
 CONSTRAINT [PK_Imagens] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

ALTER TABLE [dbo].[Imagens] ADD  CONSTRAINT [DF_Imagens_Insertdate]  DEFAULT (getdate()) FOR [Insertdate]
GO

ALTER TABLE [dbo].[Imagens]  WITH CHECK ADD  CONSTRAINT [FK_Imagens_Post] FOREIGN KEY([Post_ID])
REFERENCES [dbo].[Post] ([Id])
GO

ALTER TABLE [dbo].[Imagens] CHECK CONSTRAINT [FK_Imagens_Post]
GO




USE PortalDigital
GO

/****** Object:  Table [dbo].[Configuracoes]    Script Date: 18/10/2019 19:40:12 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Configuracoes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Phone] [varchar](15) NULL,
	[Email] [varchar](50) NULL,
	[Nome] [varchar](50) NULL,
 CONSTRAINT [PK_Configuracoes] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO


